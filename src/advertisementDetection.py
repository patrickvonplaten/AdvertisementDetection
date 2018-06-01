#import tensorflow as tf 
import numpy as np
import tensorflow as tf
from preprocessor import Preprocessor
from vgg16 import VGG16Custom
from keras.optimizers import SGD
from keras.applications import VGG16

class RecognitionSystem(object): 
    
    """
    This class should use the preproccessed data
    to train a system to recognise detection
    """
    def __init__(self, pathToDataPathesFile, pathToWeights, configs, model): 
        self.data = self.readInData(pathToDataPathesFile)
        self.testData = self.data.testData
        self.testLabels = self.data.testLabels
        self.trainData = self.data.trainData
        self.trainLabels = self.data.trainLabels
        self.configs = self.setConfigs(configs)
        self.pathToWeights = pathToWeights
        self.model = model 

    def getModel(self, flag):
        if(flag == 0):
            return VGG16Custom(input_shape = self.data.imageShape)
        else: 
            pass
            #TODO: add the network using 'imageNet' 
            #model = VGG
            #model.add(Flatten())

    def setConfigs(self, configs):
        defaultConfigs = {
            'learningRate':1e-3,
            'decay':1e-6,
            'momentum':0.9,
            'nesterov':True,
            'batch_size':8,
            'epochs':3,
            'loss':'binary_crossentropy',
            'metrics':['accuracy']
        }

        for config in configs:
            defaultConfigs[config] = configs[config]
        
        return defaultConfigs
        
    def readInData(self):
        with open(pathVariablesFile) as pathVariables:
            pathes = pathVariables.read().splitlines()
            imagesPath = pathes[0]
            labelsPath = pathes[1]
        preprocessedData = Preprocessor(imagesPath, labelsPath)
        return preprocessedData 

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

        history = self.model.fit(x, y, batch_size=self.configs['batchSize'], epochs=self.configs['numberEpoch'], verbose=2)
        self.model.save_weights(self.pathToWeights)

        print("History")
        print(history)
        """ 
        TODO: the history object should be saved in ../outputs/log/vgg16_log or 
        something like that. All data about the training process should be easily 
        be seen there 
        """

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

class Runner(object)

    def __init__(runMode, pathToConfigFile, pathToDataPathesFile, pathToWeights):
        sys.path.insert(0, pathToConfigFile)
        from configFile import getModel
        self.model = getModel()
        from configFile import getConfigs
        self.configs = getConfigs()
        recogSystem = advertisementDetection(pathToDataPathesFile =  pathToDataPathesFile,pathToWeights = pathToWeights, configs = self.configs, model = self.model)

        if(runMode == 'train'):
            recogSystem.printModelSummary()
            recogSystem.trainModel()      
       
        elif(runMode == 'evaluate'):
            recogSystem.evaluate()
           
        sys.path.remove(pathToConfigFile)

  
