#!/usr/bin/env bash

# example command
# install ffmpeg

if [ $# -eq 0 ]; then
	echo "Please state how many frames per second are to be saved as 1st argument!"
	exit
fi

advertisementDetectionPath=$(realpath ../)
mpegVideoPath="${advertisementDetectionPath}/ARD_13-03-16_19-03_Sportschau_Hamburg.mpg"
pathToSaveImages="${advertisementDetectionPath}/images"
pathToSaveLabels="${advertisementDetectionPath}/labels.txt"
pathToSavePathVariables="${advertisementDetectionPath}/src/pathVariables.txt"

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

savedImagesNum=$(ls ${pathToSaveImages} | wc -l) 

for i in `seq 1 ${savedImagesNum}`;
do
	echo "0" >> ${pathToSaveLabels}	
done  

echo "${pathToSaveImages}" >> ${pathToSavePathVariables}
echo "${pathToSaveLabels}" >> ${pathToSavePathVariables}
echo "--------------------------------------------------"
echo "Don't forget to correctly label the frames saved in ${pathToSaveImages}"
echo "--------------------------------------------------"

