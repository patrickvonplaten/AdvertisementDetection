import sys
import numpy as np
import tensorflow as tf
import pickle
from preprocessor import Preprocessor
from vgg16 import VGG16Custom
from tf.keras.optimizers import SGD
from tf.keras.applications import VGG16
from tf.keras import applications
from tf.keras.layers import Flatten, Dense
from tf.keras.models import Model, Sequential
import pickle


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

        history = self.model.fit(x, y, batch_size=self.configs['batchSize'], epochs=self.configs['epochs'], verbose='2' )
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

    def predictData(self, data):
        """
            Here we should create a function to predict the values of unseen data.
            There is no evaluation here, since there are no labels
            TODO: implement function using predict function from Keras:
            https://keras.io/models/model/
        """
        pass

