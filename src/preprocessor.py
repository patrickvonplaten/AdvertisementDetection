import numpy as np
import os
import sys
import cv2 #pip install opencv-python
from random import shuffle 
from tabulate import tabulate #pip install tabulate

class Preprocessor(object):
    
    """
    This class the path of a folder with images and a .txt file with labels
    as input and returns a numpy matrix 
    """

    def __init__(self, imagesFolderName, labelsFileName):
        self.labelsFileName = labelsFileName

        if(os.stat(self.labelsFileName).st_size == 0):
            print("Error: No labels are given in the file " + self.labelsFileName)
            print("Exit code")
            sys.exit()

        self.imagesFolderName = imagesFolderName
        self.imagesLen = len([name for name in os.listdir(imagesFolderName)]) # images start at idx = 1 
        self.splitTrainingTestData = int(0.7 * self.imagesLen)
        self.data = self.convertJPEGImageToMatrix()
        shuffle(self.data) #shuffle data set for training
        self.trainData = self.data[:self.splitTrainingTestData]
        self.testData = self.data[self.splitTrainingTestData:]

    def convertJPEGImageToMatrix(self):
        imagePath = os.path.join(self.imagesFolderName, 'image-0001.jpeg')
        image = cv2.imread(imagePath,0) 
        l = []
        labels = self.labelsFileName
        idx = 1
        with open(self.labelsFileName) as labelFile:
            for lineNum, label in enumerate(labelFile):
                imagePath = os.path.join(self.imagesFolderName, 'image-' + str(lineNum+1).zfill(5) + '.jpeg')
                image = cv2.imread(os.path.join(self.imagesFolderName, imagePath),0) #0 makes the picture black/white - for color leave out 0
                l.append((image,int(label)))
        assert(self.imagesLen == lineNum + 1), 'Make sure that the file ' + self.labelsFileName + ' has as many lines filled with labels as there are frames in the folder ' + self.imagesFolderName
        return l

    def printInformationAboutData(self): 
        labels = ['idx', 'label', 'mean', 'var', 'maxVal', 'minVal']
        table = np.zeros((self.imagesLen, len(labels)))
        for idx, entry in enumerate(self.convertJPEGImageToMatrix()): #need unshuffled images
           table[idx][0] = idx + 1
           table[idx][1] = entry[1] #label 
           table[idx][2] = np.mean(entry[0])
           table[idx][3] = np.var(entry[0])
           table[idx][4] = np.max(entry[0])
           table[idx][5] = np.min(entry[0])
        
        print('------------------------------------')
        print('Dimension of images ',self.data[0][0].shape)
        print('------------------------------------')
        print(tabulate(table, headers=labels))
        print('------------------------------------')
