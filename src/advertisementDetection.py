import sys
import os
import numpy as np
import tensorflow as tf
import pickle
from preprocessor import Preprocessor
from tensorflow.python.keras.optimizers import SGD
from tensorflow.python.keras.callbacks import TensorBoard
import pickle


class RecognitionSystem(object):

    """
    This class should use the preproccessed data
    to train a system to recognise detection
    """
    def __init__(self, data, pathToWeights, pathToSaveHistory, configs, model, indices):
        self.data = data
        self.testData = self.data.testData
        self.testLabels = self.data.testLabels
        self.trainData = self.data.trainData
        self.trainLabels = self.data.trainLabels
        self.configs = self.setConfigs(configs)
        self.pathToWeights = pathToWeights
        self.pathToSaveHistory = pathToSaveHistory
        self.model = model
        self.indices = indices

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

        os.makedirs('graph')
        tbCallBack = TensorBoard(log_dir='./graph', histogram_freq=0, write_graph=True, write_images=True)

        history = self.model.fit(x, y, batch_size=self.configs['batchSize'], epochs=self.configs['epochs'], verbose='2', callbacks=[tbCallBack] )

        # Get training and test loss histories
        training_loss = history.history['loss']
        self.training_loss = training_loss

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
        self.predictData(x,y)
        scores = self.model.evaluate(x, y, verbose=2)

        print("scalarLoss")
        print("\n%s: %.2f%%" % (self.model.metrics_names[1], scores[1]*100))

    def predictData(self, x, y):
        predictions = self.model.predict(x)
	
        # round predictions
        pred = [x[0] for x in predictions]
	
        print('All predictions:')
        print('---------------------------')
        for i in range(len(pred)):
                print('Pred: ' + str(pred[i]) + ' Label: ' + str(y[i]) + ' Index: ' + str(self.indices[i]))

        print('All false predictions:')
        print('---------------------------')
        for i in range(len(pred)):
                if(round(pred[i]) != y[i]):
                        print('Pred: ' + str(pred[i]) + ' Label: ' + str(y[i]) + ' Index: ' + str(self.indices[i]))
			
	
