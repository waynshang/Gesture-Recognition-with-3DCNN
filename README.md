# Gesture-Recognition-with-3DCNN

### In this repo I will provide 3 different way to do gesture recognition
## References Link:
1. https://research.nvidia.com/sites/default/files/pubs/2015-06_Hand-Gesture-Recognition/CVPRW2015-3DCNN.pdf
1. https://arxiv.org/pdf/1412.0767.pdf
1. http://papers.nips.cc/paper/7465-attention-in-convolutional-lstm-for-gesture-recognition.pdf

I select 6 different gestures from jester dataset   
Include swiping left, swiping right, no gesture, rolling forward, rolling backward, stop

First model:LRN+HRN can reach 0.78 accuracies
![image](https://github.com/waynshang/Gesture-Recognition-with-3DCNN/blob/master/Image/HRN%2BLRN.jpg)   
Second model: 3DCNN can reach 0.76 accuracies   
![image](https://github.com/waynshang/Gesture-Recognition-with-3DCNN/blob/master/Image/3DCNN.jpg)   
Third model: 3DCNN+ one layer LSTM / + two layer LSTM / + three layer LSTM   
![image](https://github.com/waynshang/Gesture-Recognition-with-3DCNN/blob/master/Image/3DCNN%2BLSTM.jpg)   
![image](https://github.com/waynshang/Gesture-Recognition-with-3DCNN/blob/master/Image/3DCNN%2B2LSTM.jpg)   
![image](https://github.com/waynshang/Gesture-Recognition-with-3DCNN/blob/master/Image/3DCNN%2B3LSTM.jpg)   


## You can directly type in follwing command on your terminal to execute real-time demo
```bash
python real_time/real_time.py
```
  
## result  
![image](https://github.com/waynshang/Gesture-Recognition-with-3DCNN/blob/master/Image/demo.JPG)

## Link
I also post a video on youtube:   
https://www.youtube.com/watch?v=vd0czNKL1DE   
Feel free to contact me on linkdein:   
https://www.linkedin.com/in/wayne-shang-909636166/
