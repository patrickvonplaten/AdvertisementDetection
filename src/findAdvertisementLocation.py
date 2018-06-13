import numpy as np
import cv2
import tensorflow as tf
from preprocessor import Preprocessor
from tensorflow.python.keras.applications import vgg16
from tensorflow.python.keras.models import Model, Sequential
from tensorflow.python.keras.layers import Flatten, Dense
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt  #python -mpip install -U matplotlib

#
# INPUTS FOR TESTING_____________
def readInData():
    preprocessedData = Preprocessor(imagesFolderName='../images', labelsFileName='../labels.txt', normalizeData = 0)
    return preprocessedData
_data = readInData()
_model = vgg16.VGG16(include_top = False, weights = 'imagenet', input_shape = _data.imageShape)
model = Sequential()
for layer in _model.layers:
    model.add(layer)
model.add(Flatten(name='flatten'))
model.add(Dense(1000, activation='softmax', kernel_initializer='random_uniform',bias_initializer='random_uniform'))
model.add(Dense(2, activation='softmax', kernel_initializer='random_uniform',bias_initializer='random_uniform'))
model.summary()
# _____________________________
#
class findAdvLocation(object):
    """
    trace back the network and find where the advertisement is in frame
    """

    def __init__ (self, model, testData):
        self.testData = testData
        self.model = model

    def getLayerOutput(self, input_image, layer_no):
        intermediate_layer_model = Model(inputs=self.model.input, outputs=self.model.get_layer(index = layer_no).output)
        intermediate_output = intermediate_layer_model.predict(input_image)
        return intermediate_output


    def drawGridOnImg(self):
        pass
    def showImageOnScreen(self,image):
        cv2.imshow('video',image)
        cv2.waitkey(0)
    def tracebackNetwork(self):
        testInput = obj_findAdvLocation.testData
        threshold = 0.7
        guess = obj_findAdvLocation.getLayerOutput(input_image = testInput, layer_no = -1)[0][1]
        guess = 1
        print(guess)
        if(guess>threshold):
            last_activations = obj_findAdvLocation.getLayerOutput(input_image = testInput, layer_no = -2)
            previous_activations = obj_findAdvLocation.getLayerOutput(input_image = testInput, layer_no = -4)
            print('PRINTING ABOUT ACTIVATIONS ---------------------- \n ')
            print('last layer shape', last_activations.shape)
            print('prev layer shape', previous_activations.shape)
            print('element 5,5', previous_activations[0].shape)
            K=1
            indices = np.argpartition(previous_activations,-K,axis=-3)[-K:]
            print('indices ', indices.shape)








obj_findAdvLocation = findAdvLocation(testData = _data.testData,model = model)
obj_findAdvLocation.tracebackNetwork()







img = obj_findAdvLocation.testData[0]
#cv2.imshow('result',obj_findAdvLocation.testData[0])
# dx, dy = 10,10
#
# grid_color = -1
# img[:,::dy] = grid_color
# img[::dx,:] = grid_color

width, height = 32,32
R, G, B = (0,0,255), (0,255,0), (255,0,0)

cv2.rectangle(img, (0,0), (width,height), R)
cv2.imshow('result', img)
#plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
