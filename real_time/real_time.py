#model training 是使用 jester資料5種動作


from  pynput import mouse, keyboard
from pynput.keyboard import Key
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
from keras.models import Model, load_model
import switch_1
#model1_name = ""
model1_path = "C:\\Users\\wayne\\Documents\\AIA\\final_project\\gesture_recognition_result\\save_model\\3DCNN_LRN_300_6_jester"
model1 = load_model(model1_path)
model2_path = "C:\\Users\\wayne\\Documents\\AIA\\final_project\\gesture_recognition_result\\save_model\\3DCNN_HRN_300_6_jester"
model2 = load_model(model2_path)
#字型
font = cv2.FONT_HERSHEY_SIMPLEX
quietMode = False
img_rows,img_cols=125, 57 
cap = cv2.VideoCapture(0)
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)

# set rt size as 640x480
ret = cap.set(3,640)
ret = cap.set(4,480)
framecount = 0
fps = ""
start = time.time()
frames = []
num=[5]
max =1
real_index = 5
instruction = 'no Gestrue'
pre =0
#load 種類CSV檔
class_file = 'class_jester_6_300.csv'
with open(class_file) as f:
    classes = f.readlines()
classes = [c.strip() for c in classes]
num_classes = 6
while(1):
    #fpss = cap.get(5)
    #print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fpss))
    ret, frame = cap.read()
    frame = cv2.flip(frame, 3)
    frame = cv2.resize(frame, (640,480))
    

    framecount = framecount + 1
    end  = time.time()
    timediff = (end - start)
    if( timediff >= 1):
        #timediff = end - start
        fps = 'FPS:%s' %(framecount)
        start = time.time()
        framecount = 0

    #(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
    cv2.putText(frame,fps,(10,20), font, 0.7,(0,255,0),2,1)
    X_tr=[]
         
    image=cv2.resize(frame,(img_rows,img_cols),interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    frames.append(gray)
    input=np.array(frames)
    
    if input.shape[0]==16:
        frames = []
        # print(input.shape)
        X_tr.append(input)
        X_train= np.array(X_tr)
        # print(X_train.shape)
        train_set = np.zeros((1, 16, img_cols,img_rows,3))
        train_set[0][:][:][:][:]=X_train[0,:,:,:,:]
        train_set = train_set.astype('float32')
        train_set -= 108.13708
        train_set /= 146.86292
        result_1 = model1.predict(train_set)
        result_2 = model2.predict(train_set)
        # print(result)
        num = np.argmax(result_1+result_2,axis =1)
        max = np.max((result_1+result_2)/2, axis = 1)
        # print(num[0])
        # num = 'gesture:%s' %(classes[num])
        print(classes[int(num[0])])
        input=[]
        real_index = switch_1.index_threshhold(max, int(num[0]),pre)
        # instruction = switch_1.controll_PC(real_index)
        pre = int(num[0])
    switch_1.puttext_on(max, real_index, classes, frame, font)
    # cv2.putText(frame, instruction, (450, 50), font, 0.7, (0, 255, 0), 2, 1)
    if not quietMode:
            cv2.imshow('Original',frame)
    key = cv2.waitKey(1) & 0xFF
    ## Use Esc key to close the program
    if key == 27:
        break
    elif key == ord('q'):
        quietMode = not quietMode
        print("Quiet Mode - {}".format(quietMode))
cap.release()
cv2.destroyAllWindows()
    




