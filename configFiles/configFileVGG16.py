# -*- coding: utf-8 -*-
"""VGG16 model for Keras.

# Reference

- [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556)

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import warnings

from keras.models import Model
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Input
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import GlobalAveragePooling2D
from keras.layers import GlobalMaxPooling2D
from keras.engine import get_source_inputs
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras import backend as K
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input
from keras.applications.imagenet_utils import _obtain_input_shape
from applications import vgg16 

def getModel(input_shape, classes=1):
    
    model = 


    return model

def getConfigs():
    return {
        'learningRate':1e-3,
        'decay':1e-6,
        'momentum':0.9,
        'normalizeData':True,
        'nesterov':True,
        'batchSize':8,
        'epochs':1,
        'loss':'binary_crossentropy',
        'metrics':['accuracy']
    }

