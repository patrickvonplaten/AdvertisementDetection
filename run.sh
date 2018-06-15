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

/scratch/meyer/TF_IO/Project1_ENV/GPU-Version/bin/python3 /scratch/projekt1/AdvertisementDetection/runAdvertisementDetection.py --learningRate $learningRate --logDir $TMP
cp -r $TMP/. $SCRATCHDIR


