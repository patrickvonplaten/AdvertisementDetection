#!/usr/bin/env bash
cd /Users/patrickvonplaten/AdvertisementDetection/experiment/step002_trainModel
source ../VARIABLES.sh
python ${step002Path}/dependencies/trainModel.py ${step002Path}/dependencies ${step002Path}/dependencies/pathToDataPathesFile.txt ${step002Path}/outputs/model.h5 train
