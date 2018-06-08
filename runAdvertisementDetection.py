from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import warnings
import sys
import argparse

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Flatten
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.applications import vgg16 

class Runner(object):

    def __init__(self):

        self.logDirectory, self.configs = self.parseArgs()
        self.currentDir = os.path.dirname(os.path.abspath(__file__))
        self.pathToAdvertismentDetectionSourceCode = self.currentDir + '/src'
        self.pathToDataPathesFile = self.currentDir + '/src/pathVariables.txt'
        self.pathToWeights = str(self.logDirectory) + '/model.h5'
        self.pathToSaveHistory = str(self.logDirectory) + '/history'

        sys.path.insert(0, self.pathToAdvertismentDetectionSourceCode)
        self.data = self.readInData()
        self.model = self.getModel(input_shape = self.data.imageShape)


    def start(self):
        from advertisementDetection import RecognitionSystem
        recogSystem = RecognitionSystem(data = self.data, pathToWeights = self.pathToWeights, pathToSaveHistory = self.pathToSaveHistory, configs = self.configs, model = self.model)
        recogSystem.data.printInformationAboutData()
        recogSystem.printModelSummary()
#        recogSystem.trainModel()      
#        recogSystem.evaluateModel()
      

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
        model.add(Dense(1, activation='relu'))
        model.add(Dense(classes, activation = 'sigmoid'))

        return model

    def parseArgs(self):
        configs = {
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

        parser = argparse.ArgumentParser(description='Description of your program')
        parser.add_argument('--logDir', help='The folder to save everything', required=True)
        parser.add_argument('--learningRate')
        parser.add_argument('--decay')
        parser.add_argument('--momentum')
        parser.add_argument('--batchSize')
        parser.add_argument('--epochs')
        
        args = vars(parser.parse_args())

        logDir =args['logDir']
        for arg in configs:
            if arg in args:
                configs[arg] = args[arg]

        return logDir, configs

if __name__ == "__main__":
    runner = Runner()
    runner.start()

  
