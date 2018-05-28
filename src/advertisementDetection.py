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

    def compileModel(self):
        optimizer = SGD(lr=1e-3, decay=1e-6, momentum=0.9, nesterov=True)
        loss = 'binary_crossentropy'
        metrics= ['accuracy']
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def trainModel(self):
        x = self.trainData
        y = self.trainLabels
        self.compileModel()
        
        print("Train model")
        print("-----------------------------------------------------------------")
        print("Train Data: " + str(x.shape))
        print("-----------------------------------------------------------------")

        history = self.model.fit(x, y, batch_size=self.batchSize, epochs=self.numberEpoch, verbose=2)
        self.model.save_weights('../outputs/model/vgg16_weights.h5')

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

        self.model.load_weights('../outputs/model/vgg16_weights.h5')
        
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


advertisementDetection = RecognitionSystem(batchSize = 3, numberEpoch = 2)
advertisementDetection.data.printInformationAboutData()
advertisementDetection.printModelSummary()

advertisementDetection.trainModel()
advertisementDetection.evaluateModel()
