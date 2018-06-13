#!/bin/bash

learningRate=0.001

for i in "$@"; do
	name="${i%%=*}"
	name="${name//-/_}"
	eval ${name#__}="${i#*=}"
done

echo $SGE_ROOT
SCRATCHDIR=${PWD}

# Create links and directories as needed by the actual job.
export PATH=/usr/local/cuda-9.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64:$LD_LIBRARY_PATH
export CPATH=/usr/local/include
export CUDA_HOME=/usr/local/cuda-9.0
nvidia-smi

echo $SGE_ROOT

#tfPythonPath=/tools/tensorflow/ENV_TF_GPU/bin
tfPythonPath=/scratch/meyer/TF_IO/Project1_ENV/GPU-Version/bin/

source ${tfPythonPath}/activate

cd /scratch/projekt1/AdvertisementDetection 


# Here you can start your program.
# For example: m/scyProgramm $input $param1 $param2

#${tfPythonPath}/python3 /scratch/projekt1/AdvertisementDetection/runAdvertisementDetection.py --logDir=$TMP --learningRate=$learningRate

${tfPythonPath}/python3 runAdvertisementDetection.py --logDir=$TMP --learningRate=$learningRate
cp -r $TMP/. $SCRATCHDIR
deactivate

