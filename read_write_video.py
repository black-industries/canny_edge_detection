import cv2
import numpy as np
import os
from os.path import isfile, join

def getFrame(sec, count):
    vidcap = cv2.VideoCapture('videos/testVideo.mp4')
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("videos_imgs/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames


def read_video():
    sec = 0
    frameRate = 0.5 #//it will capture image in each 0.5 second
    count=1
    success = getFrame(sec, count)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, count)


def write_video(path):
    pathIn= './'+path+'/'
    pathOut = 'video.mp4'
    fps = 0.5
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    files.sort(key = lambda x: x[5:-4])
    files.sort()
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        
        #inserting the frames into an image array
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()