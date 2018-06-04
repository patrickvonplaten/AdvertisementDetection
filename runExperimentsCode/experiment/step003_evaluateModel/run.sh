#!/usr/bin/env bash
cd /Users/patrickvonplaten/AdvertisementDetection/runExperimentsCode/experiment/step003_evaluateModel
source ../VARIABLES.sh
echo ...start ${step003Path}
python ${step003Path}/dependencies/advertisementDetection.py ${step003Path}/dependencies ${step003Path}/dependencies/pathToDataPathesFile.txt ${step003Path}/dependencies/outputsPreviousStep/model/model.h5 None evaluate
