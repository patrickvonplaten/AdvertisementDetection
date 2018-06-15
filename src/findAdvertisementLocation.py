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


    def drawGridOnAdvRegion(self, mask, image):
        for ii in range(len(mask)):
            img = image[ii]
            M = mask[ii]
            width, height = int(img.shape[0]/M.shape[0]),int(img.shape[1]/ M.shape[1])
            R, G, B = (0,0,255), (0,255,0), (255,0,0)
            #M = 18x24 output activations matrix -- normalized
            for i in range(M.shape[0]):
                for j in range( M.shape[1]):
                    if(M[i][j]):
                        cv2.rectangle(img, (j*width,i*height), ((j+1)*width,(i+1)*height), G)
            cv2.imshow('result', img)
            cv2.waitKey()
            cv2.destroyAllWindows()

    def tracebackNetwork(self,input):
        img = input

        #using: https://jacobgil.github.io/deeplearning/class-activation-maps
        Mlist = []
        for ii in range(input.shape[0]):
            class_weights = self.model.layers[-1].get_weights()[0] #0:weight 1:bias
            final_dense_layer = self.model.get_layer(index = -2).output
            get_output = K.function([self.model.layers[0].input], [final_dense_layer,self.model.get_layer(index = -1).output])
            [dense_outputs, predictions] = get_output([img])
            dense_outputs = dense_outputs[ii, :]
            class_weights = class_weights[:,ii]
            cam = np.multiply(dense_outputs,class_weights)
            cam /= np.max(cam)
            max_contribution_index = np.argmax(cam)
            print("outputs shape",dense_outputs.shape,"weights shape",class_weights.shape,"cam shape",cam.shape)
            print("max index",max_contribution_index)

            "repeat for dense-to-flatten"
            class_weights = self.model.layers[-2].get_weights()[0]
            flatten_layer = self.model.get_layer(index = -3).output
            get_output = K.function([self.model.layers[0].input], [flatten_layer,self.model.get_layer(index = -2).output])
            [flatten_outputs, predictions] = get_output([img])
            flatten_outputs = flatten_outputs[ii, :]
            class_weights = class_weights[:,ii]
            cam = np.multiply(flatten_outputs,class_weights)
            max_contribution_index = np.argmax(cam)
            max_real_val = flatten_outputs[max_contribution_index]
            cam /= np.max(cam)
            print("outputs shape",flatten_outputs.shape)
            print("weights shape",class_weights.shape)
            print("cam shape",cam.shape)
            print("max index",max_contribution_index, "value of node", flatten_outputs[max_contribution_index])
            conv_layer = self.model.get_layer(index = -4).output
            get_output = K.function([self.model.layers[0].input], [conv_layer,self.model.get_layer(index = -3).output])
            [conv_outputs, predictions] = get_output([img])
            conv_outputs = conv_outputs[ii,:]
            x,y,z = np.where(conv_outputs == max_real_val)
            M = conv_outputs[:,:,x[0]]
            if(np.max(M)):
                M /= np.max(M)+1e-6
            threshold = 0.6
            M[M>=threshold] = 1
            M[M<threshold] = 0
            print("after thresholding",M)
            Mlist.append(M)
            return Mlist
# run with
obj_findAdvLocation = findAdvLocation(testData = _data.testData,model = model)
_mask = obj_findAdvLocation.tracebackNetwork(_data.testData)
obj_findAdvLocation.drawGridOnAdvRegion(mask = _mask, image = _data.testData)
