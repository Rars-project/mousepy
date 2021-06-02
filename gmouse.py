from __future__ import print_function
from pyautogui import press, typewrite, hotkey
# from collections import OrderedDict
import cv2
import pandas as pd
import numpy as np
# import pickle
from PIL import Image
import torch
# from torch.autograd import Variable
from torchvision.transforms import *
from DemoModel import FullModel
from torch import nn
import transforms as t
import matplotlib.pyplot as plt
import json
import time
import app
import warnings
import os
def gmouse():
    warnings.filterwarnings("ignore")

    apps=["Desktop","Google Chrome","File Explorer","VLC media player"]
    with open('C:/Users/Rohan J Billava/Desktop/finalyearproject/mousepy/configs.json') as data_file:
        config = json.load(data_file)

    label_dict = pd.read_csv(config['full_labels_csv'], header=None)
    ges = label_dict[0].tolist()
    # print(ges)
    # Capture video from computer camera
    cam = cv2.VideoCapture(0)
    #cam.set(cv2.CAP_PROP_FPS, 48)
    cam.set(cv2.CAP_PROP_FPS, 60)

    # Set up some storage variables
    seq_len = 16
    value = 0
    imgs = []
    pred = 8
    top_3 = [9,8,7]
    out = np.zeros(10) # 1d array with 10 -0's
    # Load model
    print('Loading model...')

    curr_folder = 'models_jester'
    model = FullModel(batch_size=1, seq_lenght=16)
    loaded_dict = torch.load(curr_folder + '/demo.ckp') #https://pytorch.org/tutorials/beginner/saving_loading_models.html#what-is-a-state-dict
    model.load_state_dict(loaded_dict)
    model = model.cuda()
    model.eval()

    std, mean = [0.2674,  0.2676,  0.2648], [ 0.4377,  0.4047,  0.3925]
    transform = Compose([
        t.CenterCrop((96, 96)),
        t.ToTensor(),
        t.Normalize(std=std, mean=mean),
    ])

    print('Starting prediction')
    print("----------------------------------------------------------------------------")
    s = time.time()
    n = 0
    hist = []
    mean_hist = []
    setup = True
    # plt.ion()
    # fig, ax = plt.subplots()
    cooldown = 0
    eval_samples = 2
    num_classes = 27

    score_energy = torch.zeros((eval_samples, num_classes))

    while(True):
        # Capture frame-by-frame
        ret, frame = cam.read()
        #print(np.shape(frame)) # (480, 640, 3)
        # Set up input for model
        resized_frame = cv2.resize(frame, (160, 120))
        #print(np.shape(resized_frame))

        pre_img = Image.fromarray(resized_frame.astype('uint8'), 'RGB')

        #print(np.shape(pre_img))

        img = transform(pre_img)

        if n%4 == 0:
            imgs.append(torch.unsqueeze(img, 0)) #reshape

        # Get model output prediction
        if len(imgs) == 16:
            data = torch.cat(imgs).cuda()
            output = model(data.unsqueeze(0))#prediction
            out = (torch.nn.Softmax()(output).data).cpu().numpy()[0]
            if len(hist) > 300:
                mean_hist  = mean_hist[1:]
                hist  = hist[1:]
            out[-2:] = [0,0]
            hist.append(out)
            score_energy = torch.tensor(hist[-eval_samples:])
            curr_mean = torch.mean(score_energy, dim=0)
            mean_hist.append(curr_mean.cpu().numpy())
            #value, indice = torch.topk(torch.from_numpy(out), k=1)
            value, indice = torch.topk(curr_mean, k=1)
            indices = np.argmax(out)
            top_3 = out.argsort()[-3:]
            if cooldown > 0:
                cooldown = cooldown - 1
            if value.item() > 0.4 and indices < 25 and cooldown == 0: 
                print('Gesture:', ges[indices], '\t\t\t\t\t\t Value: {:.2f}'.format(value.item()))
                cooldown = 16 	
                if ges[indices] == "Stop Sign" :
                    if str(app.get_active_window_title()) == apps[0] :
                        print("Showing open apps")	
                        hotkey('win','tab')
                    elif str(app.get_active_window_title()) == apps[1] :
                        print("Switching to tab 1")	
                        hotkey('ctrl','1')
                    elif str(app.get_active_window_title()) == apps[2] :
                        print("Opening Chrome")	
                        os.system("start chrome")
                    elif str(app.get_active_window_title()) == apps[3] :
                        print("Play / Pause")	
                        hotkey('space')
                    else:
                        print("Showing open apps")	
                        hotkey('win','tab')
                        
                elif ges[indices] == "Sliding Two Fingers Right":
                    if str(app.get_active_window_title()) == apps[0] :
                        print("Opening Terminal")	
                        hotkey('win','r')
                        typewrite('cmd\n')
                    elif str(app.get_active_window_title()) == apps[1] :
                        print("Opening new tab")	
                        hotkey('ctrl','t')
                    elif str(app.get_active_window_title()) == apps[2] :
                        print("Taking Screenshot")	
                        hotkey('win','prtsc')
                    elif str(app.get_active_window_title()) == apps[3] :
                        print("Skipping 10 seconds forward")	
                        hotkey('right')
                    else:
                        print("Opening Terminal")	
                        hotkey('win','r')
                        typewrite('cmd\n')
                        
                elif ges[indices] == "Sliding Two Fingers Left":
                    if str(app.get_active_window_title()) == apps[0] :
                        print("Opening explorer")	
                        hotkey('winleft','e')
                    elif str(app.get_active_window_title()) == apps[1] :
                        print("Closing tab")	
                        hotkey('ctrl','w')
                    elif str(app.get_active_window_title()) == apps[2] :
                        print("Closing explorer")	
                        hotkey('alt','f4')
                    elif str(app.get_active_window_title()) == apps[3] :
                        print("Rewinding 10 seconds back")	
                        hotkey('left')
                    else:
                        print("Opening Explorer")	
                        hotkey('winleft','e')
                    
                elif ges[indices] == "Sliding Two Fingers Up":
                    if str(app.get_active_window_title()) == apps[0] :
                        print("Virtual Keyboard")	
                        hotkey('win','r')
                        typewrite('osk\n')
                    elif str(app.get_active_window_title()) == apps[1] :
                        print("Switching to fullscreen")	
                        hotkey('winleft','up')
                    elif str(app.get_active_window_title()) == apps[2] :
                        print("Previous folder")	
                        hotkey('backspace')
                    elif str(app.get_active_window_title()) == apps[3] :
                        print("Increasing volume")	
                        hotkey('up')
                    else:
                        print("Virtual Keyboard")	
                        hotkey('win','r')
                        typewrite('osk\n')
                        
                elif ges[indices] == "Sliding Two Fingers Down":
                    if str(app.get_active_window_title()) == apps[0] :
                        print("Opens youtube")	
                        hotkey('winleft')
                        typewrite('chrome\n','0.5')
                        typewrite('www.youtube.com\n','0.3')
                    elif str(app.get_active_window_title()) == apps[1] :
                        print("Resizing to small window")	
                        hotkey('winleft','down')
                    elif str(app.get_active_window_title()) == apps[2] :
                        print("Opening selected folder")	
                        hotkey('enter')
                    elif str(app.get_active_window_title()) == apps[3] :
                        print("Decreasing volume")	
                        hotkey('down')
                    else:
                        print("Opens youtube")	
                        hotkey('winleft')
                        typewrite('chrome\n','0.15')
                        typewrite('www.youtube.com\n')
                    
                elif ges[indices] == "Swiping Up":
                    print("Opening Chrome")	
                    os.system("start chrome")
                    
                elif ges[indices] == "Swiping Down":
                    print("Minimize All")	
                    hotkey('winleft','d')
                    
                elif ges[indices] == "Zooming In With Full Hand":
                    print("Zoom In")	
                    hotkey('winleft','+')
                    
                elif ges[indices] == "Zooming Out With Full Hand":
                    print("Zoom Out")	
                    hotkey('winleft','-')
                    
                elif ges[indices] == "Shaking Hand":
                    print("Opening Resource Monitor...")
                    hotkey('ctrl','shift','esc')
                print("")
            
            pred = indices
            imgs = imgs[1:]

            df=pd.DataFrame(mean_hist, columns=ges)

            # ax.clear()
            # df.plot.line(legend=False, figsize=(16,6),ax=ax, ylim=(0,1))
            # if setup:
            #     # plt.show(block = False)
                # setup=False
            # plt.draw()

        n += 1
        bg = np.full((480, 1200, 3), 15, np.uint8)
        
    #flipping the camera to make it easier to coordinate with gestures. 	
        frame = cv2.flip(frame, 1)
        bg[:480, :640] = frame

        font = cv2.FONT_HERSHEY_SIMPLEX
        if value > 0.4:
            cv2.putText(bg, ges[pred],(40,40), font, 1,(0,0,0),2)
        cv2.rectangle(bg,(128,48),(640-128,480-48),(0,255,0),3)
        for i, top in enumerate(top_3):
            cv2.putText(bg, ges[top],(700,200-70*i), font, 1,(255,255,255),1)
            cv2.rectangle(bg,(700,225-70*i),(int(700+out[top]*170),205-70*i),(255,255,255),3)
        
        cv2.imshow('preview',bg)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    return
if __name__ == "__main__":
    gmouse()
    