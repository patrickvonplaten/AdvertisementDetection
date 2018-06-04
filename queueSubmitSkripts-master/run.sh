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

cd /scratch/meyer/TF_IO/Source 


# Here you can start your program.
# For example: m/scyProgramm $input $param1 $param2
#echo $SCRATCHDIR
#echo $TMP
#echo --batchSize=$batchSize --iLearningRate=$iLearningRate --Beta1=$Beta1 --Beta2=$Beta2 --MeanSub=$MeanSub --logDir=$TMP --luma=1 --Large=0 --Test=1 --startPoint="new" --summaryMode=2 --maxEpochs=300 --convlayer $ConvCfg --fcLayer $DenseCfg
/tools/tensorflow/ENV_TF_GPU/bin/python3 trainSimple.py --logDir=$TMP --batchSize=$batchSize --iLearningRate=$iLearningRate --Beta1=$Beta1 --Beta2=$Beta2 --MeanSub=$MeanSub --luma=1 --startPoint="new" --summaryMode=2 --maxEpochs=300 --convlayer $ConvLayers --fcLayer $DenseLayers --GPUMem=100 --maskOption=$maskOption --batchNorm=$batchNorm --varianceOpt=$varianceOpt --varianceMaxCount=$varianceMaxCount --varianceMaxValue=$varianceMaxValue --varianceMinValue=$varianceMinValue --dropOut=$dropOut --regularisation=0 --satd=$SATD --lRelu=1 --SetPercentT=100 --SetPercentV=100 --fcLayerSize=$f1Size
cp -r $TMP/. $SCRATCHDIR
deactivate

