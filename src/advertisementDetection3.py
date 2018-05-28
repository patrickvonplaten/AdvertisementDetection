import numpy as np
import tensorflow as tf
from preprocessor import Preprocessor
from keras import applications
from keras.layers import Input, Flatten, Dense, Dropout
from keras.models import Model
from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import to_categorical


class RecognitionSystem(object):

    """
    This class should use the preproccessed data
    to train a system to recognise detection
    """
    def __init__(self):
        self.data = self.readInData()
        self.testData = self.data.testData
        self.trainData = self.data.trainData

    def readInData(self):
        with open('pathVariables.txt') as pathVariables:
            pathes = pathVariables.read().splitlines()
            imagesPath = pathes[0]
            labelsPath = pathes[1]
        preprocessedData = Preprocessor(imagesPath, labelsPath)
        return preprocessedData

check = RecognitionSystem()
check.data.printInformationAboutData()

### our data and vgg model###
train_x = []
train_y = np.zeros(len(check.trainData))
for idx, entry in enumerate(check.trainData):
    x = entry[0]
    x[:, :, 0] -= np.mean(x[:,:, 0],dtype = np.uint8)
    x[:, :, 1] -= np.mean(x[:,:, 1],dtype = np.uint8)
    x[:, :, 2] -= np.mean(x[:,:, 2],dtype = np.uint8)
    train_x.append(x)
    train_y[idx] = entry[1]
train_x = np.array(train_x)
print(train_x.shape)
print(train_y.shape)
row, col, chan = train_x[0].shape

valid_x = []
valid_y = np.zeros(len(check.testData))
for idx, entry in enumerate(check.testData):
    x = entry[0]
    x[:, :, 0] -= np.mean(x[:,:, 0],dtype = np.uint8)
    x[:, :, 1] -= np.mean(x[:,:, 1],dtype = np.uint8)
    x[:, :, 2] -= np.mean(x[:,:, 2],dtype = np.uint8)
    valid_x.append(x)
    valid_y[idx] = entry[1]



classes = 1

vgg_model = applications.VGG16(include_top=False, input_shape = (row,col,chan),weights='imagenet',pooling = 'avg')

#Create your own input format (here 3x200x200)
input = Input(shape=(row,col,3),name = 'image_input')
#Use the generated model
output_vgg16_conv = vgg_model(input)
#vgg_model.summary()

my_model = Sequential()
for lay in vgg_model.layers[0:len(vgg_model.layers)-2]:
    my_model.add(lay)

#Add a layer where input is the output of the  second last layer
#x = Dense(8, activation='softmax', name='predictions')
my_model.add(Flatten())
#my_model.add(Dense(4096, activation='relu'))
#my_model.add(Dropout(0.5))
#my_model.add(Dense(1000, activation='relu'))
#my_model.add(Dropout(0.5))


# Truncate and replace softmax layer for transfer learning
# my_model.layers.pop()
my_model.outputs = [my_model.layers[-1].output]
my_model.layers[-1].outbound_nodes = []
x = Dense(1, activation='softmax')
my_model.add(x)
my_model.summary()

sgd = SGD(lr=1e-3, decay=1e-6, momentum=0.9, nesterov=True)
#my_model.compile(optimizer=sgd, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
my_model.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['accuracy'])

batch_size = 16
nb_epoch = 1
#bin_y =  to_categorical(train_y)
my_model.fit(train_x, train_y,
          batch_size=batch_size,
          epochs=nb_epoch,
          shuffle=True,
          verbose=1,
          validation_split=0.1,
          )
