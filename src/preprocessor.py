import numpy as np
import os
import cv2 #pip install opencv-python

class Preprocessor(object):
    """
    This class the path of a folder with images and a .txt file with labels
    as input and returns a numpy matrix 
    """


    def __init__(self, imagesFolderName, labelsFileName):
        self.imagesFolderName = imagesFolderName
        self.labelsFileName = labelsFileName
        self.trainData = None 
        self.testData = None
        self.endTrainDataLine = len([name for name in os.listdir(imagesFolderName)])+1
        self.splitTrainingTestData = 0.7

    def convertJPEGImageToMatrix(self, startIdx, endIdx):
        imagePath = os.path.join(self.imagesFolderName, 'image-0001.jpeg')
        image = cv2.imread(imagePath,0) 
        l = []
        for i in range(startIdx, endIdx): 
            imagePath = os.path.join(self.imagesFolderName, 'image-' + str(i).zfill(5) + '.jpeg')
            image = cv2.imread(os.path.join(self.imagesFolderName, imagePath),0) #0 makes the picture black/white - for color leave out 0
            l.append(image)
        return l



checkThis = Preprocessor('/Users/patrickvonplaten/AdvertisementDetection/images', 'h')
print(checkThis.convertJPEGImageToMatrix(1,checkThis.endTrainDataLine))
