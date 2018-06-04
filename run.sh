#!/bin/bash

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
source /tools/tensorflow/ENV_TF_GPU/bin/activate

cd /scratch/projekt1/AdvertisementDetection 


# Here you can start your program.
# For example: m/scyProgramm $input $param1 $param2

/tools/tensorflow/ENV_TF_GPU/bin/python3 advertisementDetection.py --logDir=$TMP --learningRate=$learningRate
cp -r $TMP/. $SCRATCHDIR
deactivate

