#import tensorflow as tf 
import numpy as np
import tensorflow as tf
from preprocessor import Preprocessor
from vgg16 import VGG16

class RecognitionSystem(object): 
    
    """
    This class should use the preproccessed data
    to train a system to recognise detection
    """
    def __init__(self): 
        self.data = self.readInData()
        self.testData = self.data.testData
        self.trainData = self.data.trainData

    def readInData(self):
        with open('pathVariables.txt') as pathVariables:
            pathes = pathVariables.read().splitlines()
            imagesPath = pathes[0]
            labelsPath = pathes[1]
        preprocessedData = Preprocessor(imagesPath, labelsPath)
        return preprocessedData 

check = RecognitionSystem()
check.data.printInformationAboutData()



