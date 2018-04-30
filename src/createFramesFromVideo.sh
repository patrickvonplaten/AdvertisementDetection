#!/usr/bin/env bash

# example command
# install ffmpeg
# ./convertImages.sh $(grealpath ../ARD_13-03-16_18-36_Sportschau_TSV_MÃ¼nchen.mpg) images 0.005

if [ $# -eq 0 ]; then
	echo "Please state how many frames per second are to be saved as 1st argument!"
	exit
fi

advertisementDetectionPath=$(grealpath ../)
mpegVideoPath="${advertisementDetectionPath}/ARD_13-03-16_18-36_Sportschau_TSV_MÃ¼nchen.mpg"
pathToSaveImages="${advertisementDetectionPath}/images"
pathToSaveLabels="${advertisementDetectionPath}/labels.txt"
pathToSavePathVariables="${advertisementDetectionPath}/src/pathVariables.txt"

echo ${pathToSaveImages}

picturesPerSecond=${1} #0.005 for example will result in 3 frames for videofile
currentPath=$(pwd)

if [ -d ${pathToSaveImages} ]; then
	rm -r ${pathToSaveImages} 
fi

mkdir ${pathToSaveImages}
cd ${pathToSaveImages}
ffmpeg -i ${mpegVideoPath} -r ${picturesPerSecond} image-%05d.jpeg
cd ${currentPath}

if [ -f ${pathToSaveLabels} ];then
	rm ${pathToSaveLabels}
fi
touch ${pathToSaveLabels}

if [ -f ${pathToSavePathVariables} ];then
	rm ${pathToSavePathVariables}
fi
touch ${pathToSavePathVariables}


echo "${pathToSaveImages}" >> ${pathToSavePathVariables}
echo "${pathToSaveLabels}" >> ${pathToSavePathVariables}
echo "--------------------------------------------------"
echo "Don't forget to label the frames saved in ${pathToSaveImages}"
echo "--------------------------------------------------"

