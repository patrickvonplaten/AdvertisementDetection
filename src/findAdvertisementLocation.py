import numpy as np
import cv2
import tensorflow as tf
from preprocessor import Preprocessor
from tensorflow.python.keras.applications import vgg16
from tensorflow.python.keras.models import *
from tensorflow.python.keras.callbacks import *
from tensorflow.python.keras.layers import Flatten, Dense
from tensorflow.python.keras import backend as K


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
model.add(Dense(1, activation='softmax', kernel_initializer='random_uniform',bias_initializer='random_uniform'))
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
        intermediate_output, predictions = intermediate_layer_model.predict(input_image)
        return intermediate_output


    def drawGridOnAdvRegion(self):
        img = obj_findAdvLocation.testData[0]
        width, height = 32,32
        R, G, B = (0,0,255), (0,255,0), (255,0,0)
        #M = 18x24 output activations matrix -- normalize
        M = np.ones((18,24))
        for i in range(m):
            for j in range(n):
                if(M[i][j]>0.7):
                    cv2.rectangle(img, (j*width,i*height), ((j+1)*width,(i+1)*height), G)
        cv2.imshow('result', img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        pass

    def tracebackNetwork(self):
        testInput = self.testData
        threshold = 0.7
        #guess = self.getLayerOutput(input_image = testInput, layer_no = -1)[0][1]
        guess = 1
        print(guess)
        img = self.testData
        self.model.summary()



        class_weights = self.model.layers[-1].get_weights()[0]
        final_dense_layer = self.model.get_layer(index = -2).output
        get_output = K.function([self.model.layers[0].input], [final_dense_layer,self.model.get_layer(index = -1).output])
        [dense_outputs, predictions] = get_output([img])
        print("outputs shape",dense_outputs.shape)
        print("weights shape",class_weights.shape)
        cam = np.multiply(dense_outputs,np.transpose(class_weights))
        print("cam shape",cam.shape)
        cam /= np.max(cam)
        max_contribution_index = np.argmax(cam)
        print("max index",max_contribution_index)

        "repeat for dense-to-flatten"
        class_weights = self.model.layers[-2].get_weights()[0]
        flatten_layer = self.model.get_layer(index = -3).output
        get_output = K.function([self.model.layers[0].input], [flatten_layer,self.model.get_layer(index = -2).output])
        [flatten_outputs, predictions] = get_output([img])
        print("outputs shape",flatten_outputs.shape)
        print("weights shape",class_weights.shape)
        column_for_max_index = class_weights[:,max_contribution_index]
        cam = np.multiply(flatten_outputs,np.transpose(column_for_max_index))
        print("cam shape",cam.shape)

        cam /= np.max(cam)
        print(cam)
        max_contribution_index = np.argmax(cam)
        print("max index",max_contribution_index)

        # if(guess>threshold):
        #     last_activations = obj_findAdvLocation.getLayerOutput(input_image = testInput, layer_no = -2)
        #     previous_activations = obj_findAdvLocation.getLayerOutput(input_image = testInput, layer_no = -4)
        #     print('PRINTING ABOUT ACTIVATIONS ---------------------- \n ')
        #     print('last layer shape', last_activations.shape)
        #     print('prev layer shape', previous_activations.shape)
        #     print('element 5,5', previous_activations[0].shape)
        #     K=1
        #     indices = np.argpartition(previous_activations,-K,axis=-3)[-K:]
        #     print('indices ', indices.shape)

obj_findAdvLocation = findAdvLocation(testData = _data.testData,model = model)
obj_findAdvLocation.tracebackNetwork()
