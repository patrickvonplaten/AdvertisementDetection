#!/usr/bin/env bash
runstep003=1
runstep002=1
runstep001=0
if [ ${runstep001} == 1 ]; then
    cd /Users/patrickvonplaten/AdvertisementDetection/runExperimentsCode/experiment/step001_extractFramesForVideos
 	 ./run.sh
    cd ../
fi
if [ ${runstep002} == 1 ]; then
    cd /Users/patrickvonplaten/AdvertisementDetection/runExperimentsCode/experiment/step002_trainModel
 	 ./run.sh
    cd ../
fi
if [ ${runstep003} == 1 ]; then
    cd /Users/patrickvonplaten/AdvertisementDetection/runExperimentsCode/experiment/step003_evaluateModel
 	 ./run.sh
    cd ../
fi
