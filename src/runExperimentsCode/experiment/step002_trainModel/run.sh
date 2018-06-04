#!/usr/bin/env bash
cd /Users/patrickvonplaten/AdvertisementDetection/runExperimentsCode/experiment/step002_trainModel
source ../VARIABLES.sh
echo ...start ${step002Path}
python ${step002Path}/dependencies/advertisementDetection.py ${step002Path}/dependencies ${step002Path}/dependencies/pathToDataPathesFile.txt ${saveWeightsPath} ${saveTrainHistoryPath} train
