import numpy as np
import cv2
import tensorflow as tf
from tensorflow.python.keras.applications import vgg16
from tensorflow.python.keras.models import *
from tensorflow.python.keras.callbacks import *
from tensorflow.python.keras.layers import Flatten, Dense
from tensorflow.python.keras import backend as K
from os import listdir
from os.path import isfile, join



class findAdvLocation(object):
    """
    trace back the network and find where the advertisement is in frame
    """

    def __init__ (self, model):
        self.model = model


    def drawGridOnAdvRegion(self, mask, image):
        img = image
        M = mask
        width, height = int(img.shape[0]/M.shape[0]),int(img.shape[1]/ M.shape[1])
        R, G, B = (0,0,255), (0,255,0), (255,0,0)
        for i in range(M.shape[0]):
            for j in range( M.shape[1]):
                if(M[i][j]):
                    cv2.rectangle(img, (j*width,i*height), ((j+1)*width,(i+1)*height), G)
        cv2.imshow('result', img)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def tracebackNetwork(self,input):
        # get outputs of dense, flatten, last convolution layers
        # get weights between (1)dense-output (2) flatten-dense
        img = input
        class_weights_1 = self.model.layers[-1].get_weights()[0] #0:weight 1:bias
        print("1 weights shape",class_weights_1.shape)
        final_dense_layer = self.model.get_layer(index = -2).output
        get_output = K.function([self.model.layers[0].input], [final_dense_layer])
        dense_outputs = get_output([img])[0]
        class_weights_2 = self.model.layers[-2].get_weights()[0]
        print("2 weights shape",class_weights_2.shape)
        flatten_layer = self.model.get_layer(index = -3).output
        get_output = K.function([self.model.layers[0].input], [flatten_layer])
        flatten_outputs = get_output([img])[0]
        conv_layer = self.model.get_layer(index = -4).output
        get_output = K.function([self.model.layers[0].input], [conv_layer])
        conv_outputs = get_output([img])[0]
        print("outputs shape: dense-flatten-conv",dense_outputs.shape,flatten_outputs.shape,conv_outputs.shape)
        conv_outputs = conv_outputs[0,:]
        dense_outputs = dense_outputs[0, :]
        flatten_outputs = flatten_outputs[0,:]
        #
        # calculate contribution to activation map
        # normally (1,1000)x(1000,1) = (1,1)
        # but we need to compare 1000 multiplications before they are summed up
        # so we do elementwise multiplication here
        cam = np.multiply(dense_outputs,class_weights_1[:,0])
        print(np.max(cam))
        T = 0.8 #threshold: choose largest contribution nodes of dense layer
        max_contribution_indexes_dense = np.where(cam>(T*np.max(cam)))[0]
        print('idx dense', max_contribution_indexes_dense)
        M = np.zeros_like(conv_outputs[:,:,0]) # initialize mask in the size of conv filters
        #
        #loop over maximum cam dense nodes and track the contribution of flatten to this nodes
        for ii in range(len(max_contribution_indexes_dense)):
            max_contribution_index = max_contribution_indexes_dense[ii]
            # multiply flatten layer outputs only with the ii'th column of weights
            # because we know they give max effect to dense
            cam = np.multiply(flatten_outputs,class_weights_2[:,max_contribution_index])
            print('flatten max value',np.max(cam))
            threshold = 0.8
            # search largest flatten layer nodes that are contributing most
            max_contribution_indexes_flatten = np.where(cam>(threshold*np.max(cam)))[0]
            print('idx flatten',max_contribution_indexes_flatten)
            for jj in range(len(max_contribution_indexes_flatten)):
                max_real_val = flatten_outputs[max_contribution_indexes_flatten[jj]]
                x,y,z = np.where(conv_outputs == max_real_val) # find the same node at conv filter
                M[x[0],y[0]] = 1 # mark that coordinate
        return M
#____________read images
"place the images in images folder."
mypath='images'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
imageDataList = []
for n in range(0, len(onlyfiles)):
    image = cv2.imread( join(mypath,onlyfiles[n]) )
    image = cv2.resize(image, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
    imageDataList.append(image)
print('**********', len(onlyfiles),'images loaded!')

#_________________LOAD MODEL____________
_model = vgg16.VGG16(include_top = False, weights = 'imagenet', input_shape = imageDataList[0].shape)
model = Sequential()
for layer in _model.layers:
    model.add(layer)
model.add(Flatten(name='flatten'))
model.add(Dense(1000, activation='relu'))
model.add(Dense(1, activation = 'sigmoid'))
model.load_weights('model0001ep15.h5')
#model.summary()
# _____________________________
#
#run
for ii in range(len(imageDataList)):
    sample = np.concatenate(imageDataList[ii]).reshape((1,) + imageDataList[ii].shape)
    obj_findAdvLocation = findAdvLocation(model = model)
    _mask = obj_findAdvLocation.tracebackNetwork(sample)
    obj_findAdvLocation.drawGridOnAdvRegion(mask = _mask, image = imageDataList[ii])
