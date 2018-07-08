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



class AdvertisementLocator(object):
    """
    trace back the network and find where the advertisement is in frame
    """

    def __init__ (self, imagesDirPath, weightFilePath):
        self.imagesDirPath = imagesDirPath
        self.weightFilePath = weightFilePath
        self.images = self.loadImages()
        self.imageShape = self.images[0].shape
        self.model = self.loadModel()
        self.threshold = 0.6
        self.outputToDenseWeights = self.model.layers[-1].get_weights()[0] #0:weight 1:bias
        print("Output to Dense",self.outputToDenseWeights.shape)
        self.denseToFlattenWeights = self.model.layers[-2].get_weights()[0]
        print("Dense to Flatten",self.denseToFlattenWeights.shape)

    def loadModel(self):
        vgg16Model = vgg16.VGG16(include_top = False, weights = 'imagenet', input_shape = self.imageShape)
        model = Sequential()

        for layer in vgg16Model.layers:
            model.add(layer)
        model.add(Flatten(name='flatten'))
        model.add(Dense(1000, activation='relu'))
        model.add(Dense(1, activation = 'sigmoid'))
        model.load_weights(self.weightFilePath)

        return model

    def loadImages(self):
        imageFiles = [ imageFile for imageFile in listdir(self.imagesDirPath) if isfile(join(self.imagesDirPath,imageFile)) ]
        images = []

        for imageFile in imageFiles:
            image = cv2.imread( join(self.imagesDirPath,imageFile) )
            image = cv2.resize(image, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
            images.append(image)

        print('**********', len(images),'images loaded!')
        return images


    def drawGridOnAdvRegion(self, mask, image):


        width, height = int(image.shape[0]/mask.shape[0]),int(image.shape[1]/ mask.shape[1])
        R, G, B = (0,0,255), (0,255,0), (255,0,0)
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                if(mask[i][j]):
                    cv2.rectangle(image, (j*width,i*height), ((j+1)*width,(i+1)*height), R)
        cv2.imshow('result', image)
        cv2.waitKey(0)
#        cv2.destroyAllWindows()

    def getConvOutputs(self, image):
        convLayer = self.model.get_layer(index = -4).output
        getOutputFn = K.function([self.model.layers[0].input], [convLayer])
        return getOutputFn([image])[0][0,:]

    def getDenseOutputs(self, image):
        finalDenseLayer = self.model.get_layer(index = -2).output
        getOutputFn = K.function([self.model.layers[0].input], [finalDenseLayer])
        return getOutputFn([image])[0][0,:]

    def getFlattenOutputs(self, image):
        flattenLayer = self.model.get_layer(index = -3).output
        getOutputFn = K.function([self.model.layers[0].input], [flattenLayer])
        return getOutputFn([image])[0][0,:]

    def tracebackNetwork(self, image):

        flattenOutputs = self.getFlattenOutputs(image)
        denseOutputs = self.getDenseOutputs(image)
        convOutputs = self.getConvOutputs(image)

        print("Flatten",flattenOutputs.shape)
        print("Dense",denseOutputs.shape)
        print("conv",convOutputs.shape)

        classActivationMapDensetoOutput = np.multiply(denseOutputs,self.outputToDenseWeights[:,0])
        
#                (self.threshold*np.max(classActivationMap)))[0]

        #print("Indexes",maxContributionIndexesDense)

        mask = np.zeros_like(convOutputs[:,:,0])

        dummyIndexArrayFlatten = np.arange(len(flattenOutputs))
        dummyIndexArrayConv = dummyIndexArrayFlatten.reshape(convOutputs.shape)

        classActivationMapFlattenandDense = np.zeros_like(flattenOutputs)
        for idx,weightedActivation in enumerate(classActivationMapDensetoOutput):

            classActivationMapFlattenandDense += weightedActivation*np.multiply(flattenOutputs,self.denseToFlattenWeights[:,idx])
            #sum of contribution of dense layer weighted with flatten layer
        maxOfclassActivationMapFlattenandDense = np.max(classActivationMapFlattenandDense)
        maxContributionIndexesDenseFlatten = np.where(classActivationMapFlattenandDense > (self.threshold*maxOfclassActivationMapFlattenandDense))[0]
        for maxIdxFlat in maxContributionIndexesDenseFlatten:
            print(flattenOutputs[maxIdxFlat])
            x,y,z = np.where(dummyIndexArrayConv == maxIdxFlat)
            #assert len(x) == len(y) == 1, "Array should only have one value"
            mask[x[0],y[0]] = 1


        # c = 0.6*np.max(mask)
        # mask[mask<c] = 0
        # mask[mask>=c] = 1
        return mask

if __name__ == "__main__":

    advLocator = AdvertisementLocator('images','model.h5')
    images = advLocator.images
    for image in images:
        reshapedImageForTraceback = np.concatenate(image).reshape((1,) + image.shape)
        mask = advLocator.tracebackNetwork(reshapedImageForTraceback)
        advLocator.drawGridOnAdvRegion(mask = mask, image = image)
