import numpy as np
import cv2
import tensorflow as tf
from preprocessor import Preprocessor
from tensorflow.python.keras.applications import vgg16
from tensorflow.python.keras.models import Model, Sequential
from tensorflow.python.keras.layers import Flatten, Dense, Input,Reshape, Dropout
import matplotlib.pyplot as plt





preprocessedData = Preprocessor(imagesFolderName='../images', labelsFileName='../labels.txt', normalizeData = 0)
X = preprocessedData.testData
cv2.imshow('dsd',X[0])
cv2.waitKey()


inputs = Input(shape=X[0].shape)
prediction = Flatten()(inputs)
re = Reshape((576,768,3))(prediction)
print('in',inputs.shape)
model = Model(inputs=inputs, outputs=re)
print('out',re.shape)
y = model.predict(X)
print(y.shape)
#y=np.reshape(y[0],(576,768,3))
#y=np.transpose(y)
model.summary()

cv2.imshow('dsda',y[0])
cv2.waitKey()
cv2.destroyAllWindows()
