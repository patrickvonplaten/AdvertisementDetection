#import tensorflow as tf 
import numpy as np
import tensorflow as tf
from preprocessor import Preprocessor
from vgg16 import VGG16
from keras.optimizers import SGD

class RecognitionSystem(object): 
    
    """
    This class should use the preproccessed data
    to train a system to recognise detection
    """
    def __init__(self, batchSize, numberEpoch): 
        self.data = self.readInData()
        self.testData = self.data.testData
        self.testLabels = self.data.testLabels
        self.trainData = self.data.trainData
        self.trainLabels = self.data.trainLabels
        self.batchSize = batchSize
        self.numberEpoch = numberEpoch
        self.model = VGG16(input_shape = self.data.imageShape)

    def readInData(self):
        with open('pathVariables.txt') as pathVariables:
            pathes = pathVariables.read().splitlines()
            imagesPath = pathes[0]
            labelsPath = pathes[1]
        preprocessedData = Preprocessor(imagesPath, labelsPath)
        return preprocessedData 

    def printModelSummary(self):
        print('Model Summary')
        self.model.summary()

    def trainModel(self):
        optimizer = SGD(lr=1e-3, decay=1e-6, momentum=0.9, nesterov=True)
        loss = 'binary_crossentropy'
        metrics= ['accuracy']
        x = self.trainData
        y = self.trainLabels
        print(x.shape)

        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
        self.model.fit(x, y, batch_size=self.batchSize, epochs=self.numberEpoch)

advertisementDetection = RecognitionSystem(16, 1)
advertisementDetection.data.printInformationAboutData()
advertisementDetection.printModelSummary()

# Trying to train the model will take forever
# advertisementDetection.trainModel()
