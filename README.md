# AdvertisementDetection

Building a tensorflow model to recognize whether a picture 
contains advertisment or not.

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

## TODO
Here we should write down 
the todo list

- [x] add preprocessor to convert video to numpy matrix  
- [x] find good tensorflow model similar to Inception-v3 -> vgg16
- [x] build structure of model
- [ ] try out different structures of model and run on cluster in vgg16.py
- [ ] complete TODO's in advertisementDetection.py
- [ ] add substract average function in preprocessing.py similar to the one in advertisementDetection3.py 
