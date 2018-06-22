concurrent advertisementDetection:
    trainingCorpus 1 

concurrent advertisementDetection
parallel advertisementDetectionTrainingEvaluation(qsub="-hard -l h_vmem=15G -l h_rt=80:00:00 -l gpu=1"):
    curPath=$(pwd)
    /u/platen/virtualenvironment/AdvertismentDetection/bin/python runAdvertisementDetection.py --logDir=results 
    cd ${curPath}

