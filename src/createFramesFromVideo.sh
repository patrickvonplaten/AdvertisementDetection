#!/usr/bin/env bash

# example command
# install ffmpeg
# ./convertImages.sh $(grealpath ../ARD_13-03-16_18-36_Sportschau_TSV_MÃ¼nchen.mpg) images 0.005

mpegVideoPath='/Users/patrickvonplaten/AdvertisementDetection/ARD_13-03-16_18-36_Sportschau_TSV_MÃ¼nchen.mpg'
pathToSaveImages='/Users/patrickvonplaten/AdvertisementDetection/images'
picturesPerSecond=${1} #0.005 for example will result in 3 frames for videofile

currentPath=$(pwd)
if [ -f ${pathToSaveImages} ]; then
	rm -r ${pathToSaveImages} 
fi

mkdir ${pathToSaveImages}
cd ${pathToSaveImages}
ffmpeg -i ${mpegVideoPath} -r ${picturesPerSecond} image-%05d.jpeg
cd ${currentPath}



