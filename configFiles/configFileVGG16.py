from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import warnings

from keras.models import Model, Sequential
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Input
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import GlobalAveragePooling2D
from keras.layers import GlobalMaxPooling2D
from keras.engine import get_source_inputs
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras import backend as K
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input
from keras.applications.imagenet_utils import _obtain_input_shape
from keras.applications import vgg16 

class Runner(object):

    def __init__(self, pathToAdvertismentDetection,  listOfConfigs=listOfConfigs, logDirectory=logDirectory):

        self.pathToAdvertismentDetectionSourceCode = '/Users/patrickvonplaten/AdvertisementDetection/src'
        self.pathToDataPathesFile = '/Users/patrickvonplaten/AdvertisementDetection/src/pathVariables.txt' 
        self.pathToWeights = str(logDirectory) + '/model.h5'
        self.pathToSaveHistory = str(logDirectory) + '/history'

        sys.path.insert(0, self.pathToAdvertismentDetectionSourceCode)
        self.configs = self.parseConfigsToDict(listOfConfigs) 
        self.data = self.readInData()
        self.model = self.getModel(input_shape = self.data.imageShape)


    def start(self):
        from advertisementDetection import RecognitionSystem 
        recogSystem = RecognitionSystem(data = self.data, pathToWeights = self.pathToWeights, pathToSaveHistory = self.pathToSaveHistory, configs = self.configs, model = self.model)
        recogSystem.printModelSummary()
        recogSystem.trainModel()      
        recogSystem.evaluateModel()
      

    def readInData(self):
        with open(self.pathToDataPathesFile) as pathVariables:
            pathes = pathVariables.read().splitlines()
            imagesPath = pathes[0]
            labelsPath = pathes[1]
        normalizeData = self.configs['normalizeData'] if 'normalizeData' in self.configs else False
        from advertisementDetection import Preprocessor 
        preprocessedData = Preprocessor(imagesPath, labelsPath, normalizeData = normalizeData)
        return preprocessedData 


    def getModel(self, input_shape, classes=1):
        vgg16_model = vgg16.VGG16(include_top = False, input_shape = input_shape)

        model = Sequential()
        for layer in vgg16_model.layers:
            model.add(layer)
        for layer in model.layers:
            layer.trainable = False

        model.add(Flatten(name='flatten'))
        model.add(Dense(4096, activation='relu'))
        model.add(Dense(classes, activation = 'sigmoid'))

        return model

    def parseConfigsToDict(self, listOfConfigs):
        defaultConfigs =  {
            'learningRate':1e-3,
            'decay':1e-6,
            'momentum':0.9,
    #        'normalizeData':True,
            'nesterov':True,
            'batchSize':8,
            'epochs':1,
            'loss':'binary_crossentropy',
            'metrics':['accuracy']
        }
        print(listOfConfigs)

        return defaultConfigs

if __name__ == "__main__":
    logDirectory = sys.argv[1]
    listOfConfigs = sys.argv[2:]

    runner = Runner(listOfConfigs=listOfConfigs, logDirectory=logDirectory)

  
