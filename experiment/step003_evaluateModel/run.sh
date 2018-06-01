#!/usr/bin/env bash
cd /Users/patrickvonplaten/AdvertisementDetection/experiment/step003_evaluateModel
source ../VARIABLES.sh
python ${step003Path}/dependencies/evaluateModel.py ${step003Path}/dependencies ${step003Path}/dependencies/pathToDataPathesFile.txt ${step003Path}/dependencies/outputsPreviousStep/model.h5 train
