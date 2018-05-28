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

def VGG16(input_shape, weights=None, classes=1):
    
    img_input = Input(shape=input_shape)

    # Block 1
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv1')(img_input)
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv2')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool')(x)

    # Block 2
#    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv1')(x)
#    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv2')(x)
#    x = MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool')(x)
#
    # Block 3
#    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv1')(x)
#    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv2')(x)
#    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv3')(x)
#    x = MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool')(x)
#
    # Block 4
#    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv1')(x)
#    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv2')(x)
#    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv3')(x)
#    x = MaxPooling2D((2, 2), strides=(2, 2), name='block4_pool')(x)
#
    # Block 5
#    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv1')(x)
#    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv2')(x)
#    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='block5_conv3')(x)
#    x = MaxPooling2D((2, 2), strides=(2, 2), name='block5_pool')(x)

    # Classification block
    x = Flatten(name='flatten')(x)
    #x = Dense(4096, activation='relu', name='fc1')(x) #this gives crazy amount of parameters -> ask whether this is ok
    #x = Dense(4096, activation='relu', name='fc2')(x) #this gives crazy amount of parameters -> ask whether this is ok
    x = Dense(3, activation='relu', name='fc1')(x) #this gives crazy amount of parameters -> ask whether this is ok
    x = Dense(classes, activation='sigmoid', name='predictions')(x)

    inputs = img_input

    # Create model.
    model = Model(inputs, x, name='vgg16')

    # load weights
    if weights is not None:
        model.load_weights(weights)

    return model
