import sys
import numpy as np
import tensorflow as tf
import pickle
from preprocessor import Preprocessor
from vgg16 import VGG16Custom
from keras.optimizers import SGD
from keras.applications import VGG16

class RecognitionSystem(object): 
    
    """
    This class should use the preproccessed data
    to train a system to recognise detection
    """
    def __init__(self, data, pathToWeights, pathToSaveHistory, configs, model): 
        self.data = data 
        self.testData = self.data.testData
        self.testLabels = self.data.testLabels
        self.trainData = self.data.trainData
        self.trainLabels = self.data.trainLabels
        self.configs = self.setConfigs(configs)
        self.pathToWeights = pathToWeights
        self.pathToSaveHistory = pathToSaveHistory
        self.model = model

    def setConfigs(self, configs):
        defaultConfigs = {
            'learningRate':1e-3,
            'decay':1e-6,
            'momentum':0.9,
            'nesterov':True,
            'batchSize':8,
            'epochs':3,
            'loss':'binary_crossentropy',
            'metrics':['accuracy']
        }

        for config in configs:
            defaultConfigs[config] = configs[config]
        
        return defaultConfigs
        
    def printModelSummary(self):
        print('Model Summary')
        self.model.summary()

    def compileModel(self):
        optimizer = SGD(lr=self.configs['learningRate'], decay=self.configs['decay'], momentum=self.configs['momentum'], nesterov=self.configs['nesterov'])
        self.model.compile(optimizer=optimizer, loss=self.configs['loss'], metrics=self.configs['metrics'])

    def trainModel(self):
        x = self.trainData
        y = self.trainLabels
        self.compileModel()
        
        print("Train model")
        print("-----------------------------------------------------------------")
        print("Train Data: " + str(x.shape))
        print("-----------------------------------------------------------------")

        history = self.model.fit(x, y, batch_size=self.configs['batchSize'], epochs=self.configs['epochs'], verbose=2)
        self.model.save_weights(self.pathToWeights)

        with open(self.pathToSaveHistory, 'wb') as pickleFile:
            pickle.dump(history.history, pickleFile)

    def evaluateModel(self):
        x = self.testData
        y = self.testLabels 
        self.compileModel()

        self.model.load_weights(self.pathToWeights)
        
        print("Decode model")
        print("-----------------------------------------------------------------")

        scalarLoss = self.model.evaluate(x, y, verbose=2)

        print("scalarLoss")
        print(scalarLoss)
        """ 
        TODO: the scalarLoss should be saved as well somewhere like  ../outputs/result/vgg16_result or 
        something like that. It should show the percentage of correctly labeled data and for each frame it should show correct label vs. predicted label. 
        """

    def predictData(self, data):
        """
            Here we should create a function to predict the values of unseen data.
            There is no evaluation here, since there are no labels 
            TODO: implement function using predict function from Keras:
            https://keras.io/models/model/
        """
        pass

class Runner(object):

    def __init__(self, pathToConfigFile, pathToDataPathesFile, pathToWeights, pathToSaveHistory, runMode):
        self.pathToConfigFile = str(pathToConfigFile)
        self.pathToDataPathesFile = str(pathToDataPathesFile)
        self.pathToWeights = str(pathToWeights)
        self.pathToSaveHistory = str(pathToSaveHistory)
        self.runMode = str(runMode)

        sys.path.insert(0, self.pathToConfigFile)

        from configFile import getConfigs
        self.configs = getConfigs()

        self.data = self.readInData()

        from configFile import getModel
        self.model = getModel(input_shape = self.data.imageShape)


    def start(self):
        recogSystem = RecognitionSystem(data = self.data, pathToWeights = self.pathToWeights, pathToSaveHistory = self.pathToSaveHistory, configs = self.configs, model = self.model)
        if(self.runMode == 'train'):
            recogSystem.printModelSummary()
            recogSystem.trainModel()      
       
        elif(self.runMode == 'evaluate'):
            recogSystem.evaluateModel()
      
    def clean(self):
        sys.path.remove(self.pathToConfigFile)

    def readInData(self):
        with open(self.pathToDataPathesFile) as pathVariables:
            pathes = pathVariables.read().splitlines()
            imagesPath = pathes[0]
            labelsPath = pathes[1]
        normalizeData = self.configs['normizeData'] if 'normalizeData' in self.configs else False
        preprocessedData = Preprocessor(imagesPath, labelsPath, normalizeData = normalizeData)
        return preprocessedData 

if __name__ == "__main__":
    pathToConfigFile = sys.argv[1]
    pathToDataPathesFile = sys.argv[2]
    pathToWeights = sys.argv[3]
    pathToSaveHistory = sys.argv[4]
    runMode = sys.argv[5]

    runner = Runner(pathToConfigFile = pathToConfigFile,  pathToDataPathesFile = pathToDataPathesFile,  pathToWeights = pathToWeights, pathToSaveHistory = pathToSaveHistory, runMode = runMode)
    runner.start()
    runner.clean()

  
