#!/usr/bin/env bash
cd /Users/patrickvonplaten/AdvertisementDetection/experiment/step001_extractFramesForVideos
source ../VARIABLES.sh
cd outputs
mkdir images 
cd images 
ffmpeg -i ${pathToVideo} -r ${rateToConvertVideosToFrames} image-%05d.jpeg
cd ..
cp ${step001Labels} labels.txt
cd /Users/patrickvonplaten/AdvertisementDetection/experiment/step001_extractFramesForVideos
