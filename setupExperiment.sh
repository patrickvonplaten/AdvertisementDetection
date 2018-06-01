#!/usr/bin/env bash

#This file is there to set up an experiment

#sys.path.insert(0, '/path/to/application/app/folder')
#sys.path.remove('/path/to/application/app/folder')


pathToVideo="/Users/patrickvonplaten/AdvertisementDetection/ARD_13-03-16_18-36_Sportschau_TSV_MÃ¼nchen.mpg"
rateToConvertVideosToFrames=0.8
# labels must correspond to both video and the rate so that they match
labels=/Users/patrickvonplaten/AdvertisementDetection/correctLabels/correctlabels08.txt

nameOfExperiment=experiment

function createStepDir {
	stepPath=${1}
	previousStep=${2}
	step=${3}
	currentPath=$(pwd)

	mkdir ${stepPath}
	echo "${step}Path=${stepPath}" >> VARIABLES.sh
	runstep="run${step}"
	runStepNameAsVariable='${'"${runstep}"'}'

	awk -v var="${runstep}=1" 'NR==1{print; print var} NR!=1' runMain.sh > temp && mv temp runMain.sh 
	chmod +x runMain.sh
	echo "if [ ${runStepNameAsVariable} == 1 ]; then" >> runMain.sh
	echo "    cd ${stepPath}" >> runMain.sh
	echo " 	 ./run.sh" >> runMain.sh
	echo "    cd ../" >> runMain.sh
	echo "fi" >> runMain.sh

	echo ".${stepPath}/clean.sh" >> clean.sh

	cd ${stepPath} 
	mkdir dependencies
	mkdir outputs
	touch run.sh
	echo "#!/usr/bin/env bash" >> run.sh
	chmod +x run.sh
	touch clean.sh 
	echo "#!/usr/bin/env bash" >> clean.sh
	chmod +x clean.sh

	echo "rm -r ./outputs" >> clean.sh

	echo "cd ${stepPath}" >> run.sh
	echo "source ../VARIABLES.sh" >> run.sh

	if [ ${previousStep} != "None" ]; then 
		ln -s ${previousStep}/outputs dependencies/outputsPreviousStep
	fi

	cd ${currentPath}
}

if [ -d ${nameOfExperiment} ]; then
	echo "Setup already exists!!!"
	exit
fi

currentPath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
setupPath=${currentPath}/${nameOfExperiment}

mkdir ${setupPath}
cd ${setupPath}

touch VARIABLES.sh
touch runMain.sh
echo "#!/usr/bin/env bash" >> runMain.sh
chmod +x runMain.sh
touch clean.sh
echo "#!/usr/bin/env bash" >> clean.sh
chmod +x clean.sh

echo "pathToVideo=${pathToVideo}" >> VARIABLES.sh
echo "rateToConvertVideosToFrames=${rateToConvertVideosToFrames}" >> VARIABLES.sh
echo "step001Labels=${labels}" >> VARIABLES.sh

###############step001###################
cd ${setupPath}
step001Path=${setupPath}/step001_extractFramesForVideos
createStepDir ${step001Path} "None" step001
step001RunFile=${step001Path}/run.sh

echo "cd outputs" >> ${step001RunFile}
echo "mkdir images " >> ${step001RunFile}
echo "cd images " >> ${step001RunFile}
echo 'ffmpeg -i ${pathToVideo} -r ${rateToConvertVideosToFrames} image-%05d.jpeg' >> ${step001RunFile}
echo "cd .." >> ${step001RunFile}
echo 'cp ${step001Labels} labels.txt' >> ${step001RunFile}
echo "cd ${step001Path}" >> ${step001RunFile}

#############step002####################
cd ${setupPath}
step002Path=${setupPath}/step002_trainModel
createStepDir ${step002Path} "${step001Path}" step002
step002RunFile=${step002Path}/run.sh
ln -s ${advertisementDetectionPath} ${step002Path}/dependencies/trainModel.py
touch ${step002Path}/dependencies/pathToDataPathesFile.txt
echo "$(realpath ${step002Path}/dependencies/outputsPreviousStep/images)" >> pathToDataPathesFile.txt
echo "$(realpath ${step002Path}/dependencies/outputsPreviousStep/labels.txt)" >> pathToDataPathesFile.txt
cp ${configFile} ${step002Path}/dependencies/configFile.py

echo 'python ${step002Path}/dependencies/trainModel.py ${step002Path}/dependencies/configFile.py ${step002Path}/dependencies/pathToDataPathesFile.txt ${step002Path}/outputs/model.h5}' >> ${step002RunFile}



















