# AdvertisementDetection

In this university project, we manually labeled 1000 pictures sampled from german 
football videos und used the VGG-16 model architecture to classify the pictures to "showing advertisment panel" 
or "not showing advertisment panel".

# How to run code

- install python3
- check createFramesFromVideo.sh - path of video file should correspond to to that in code
- install ffmpeg
- pip install opencv-python
- pip install tabulate
- install tensorflow
- pip install keras

1. create frames from video using createFramesFromVideo.sh
	- ./createFramesFromVideo.sh 0.005 -> 0.005 frames per second
2. label frames
3. run python advertisementDetection.py
