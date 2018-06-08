#!/usr/bin/env bash

# example command
# install ffmpeg

if [ $# -eq 0 ]; then
	echo "Please state the three frames per second rations are to be inserted as 1st, 2nd, 3rd argument!"
	exit
fi

advertisementDetectionPath=$(realpath ../)
mpegVideoPath1="${advertisementDetectionPath}/ARD_13-03-16_18-36_Sportschau_TSV_MÃ¼nchen.mpg"
mpegVideoPath2="${advertisementDetectionPath}/ARD_13-03-16_18-48_Sportschau_Bremen.mpg"
mpegVideoPath3="${advertisementDetectionPath}/ARD_13-03-16_19-03_Sportschau_Hamburg.mpg"
pathToSaveImages="${advertisementDetectionPath}/images"
pathToSaveLabels="${advertisementDetectionPath}/labels.txt"
pathToSavePathVariables="${advertisementDetectionPath}/src/pathVariables.txt"

picturesPerSecond1=${1} #0.005 for example will result in 3 frames for videofile
picturesPerSecond2=${2} #0.005 for example will result in 3 frames for videofile
picturesPerSecond3=${3} #0.005 for example will result in 3 frames for videofile

currentPath=$(pwd)

if [ -d ${pathToSaveImages} ]; then
	rm -r ${pathToSaveImages} 
fi

mkdir ${pathToSaveImages}
cd ${pathToSaveImages}
ffmpeg -i ${mpegVideoPath1} -r ${picturesPerSecond1} image-%05d.jpeg
savedImagesNum=$(ls ${pathToSaveImages} | wc -l) 
mkdir temp
cd temp
ffmpeg -i ${mpegVideoPath2} -r ${picturesPerSecond2} image-%05d.jpeg
savedImagesNew=$(ls ${pathToSaveImages}/temp | wc -l) 
echo $savedImagesNew
touch log.txt

for i in $(seq -f "%05g" 1 ${savedImagesNew})
do
	counter=$(printf "%05d" $((10#${i} + ${savedImagesNum})))

	imageNameNew="${pathToSaveImages}/image-${counter}.jpeg"
	imageNameOld="image-${i}.jpeg"
	mv ${imageNameOld} ${imageNameNew}
done
cd ${pathToSaveImages}
rm -r temp

savedImagesNum=$(ls ${pathToSaveImages} | wc -l) 
mkdir temp 
cd temp
ffmpeg -i ${mpegVideoPath3} -r ${picturesPerSecond3} image-%05d.jpeg
savedImagesNew=$(ls ${pathToSaveImages}/temp | wc -l) 
for i in $(seq -f "%05g" 1 ${savedImagesNew})
do
	counter=$(printf "%05d" $((10#${i} + ${savedImagesNum})))

	imageNameNew="${pathToSaveImages}/image-${counter}.jpeg"
	imageNameOld="image-${i}.jpeg"
	mv ${imageNameOld} ${imageNameNew}
done
cd ${pathToSaveImages}
rm -r temp

savedImagesNum=$(ls ${pathToSaveImages} | wc -l) 
cd ${currentPath}

if [ -f ${pathToSaveLabels} ];then
	rm ${pathToSaveLabels}
fi
touch ${pathToSaveLabels}

if [ -f ${pathToSavePathVariables} ];then
	rm ${pathToSavePathVariables}
fi
touch ${pathToSavePathVariables}


for i in `seq 1 ${savedImagesNum}`;
do
	echo "0" >> ${pathToSaveLabels}	
done  

echo "${pathToSaveImages}" >> ${pathToSavePathVariables}
echo "${pathToSaveLabels}" >> ${pathToSavePathVariables}
echo "--------------------------------------------------"
echo "Don't forget to correctly label the frames saved in ${pathToSaveImages}"
echo "--------------------------------------------------"

