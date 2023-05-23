import os
import subprocess

#cameraAdapterStart
import cv2
index = 0
arr = []
while True:
    cap = cv2.VideoCapture(index)
    try:
        if cap.getBackendName()=="MSMF":
            arr.append(index)
    except:
        break
    cap.release()
    index += 1

from tkinter import *
import tkinter as tk

# create an instance of tkinter
win = tk.Tk()

#Define the size of the window
win.geometry("400x200")

#Name the title of the window
win.title("Select Camera")

# number of buttons
n=len(arr)

my_str=tk.StringVar()
l1=tk.Label(win, textvariable=my_str, width=60)
l1.grid(row=1, column=60, columnspan=60)
#Defining the row and column
i=3

#Iterating over the numbers till n and
#creating the button
def yolov5(k):
    subprocess.call('python detect.py --source ' + str(k))
for j in range(n):
    e = Button(win, text='Camera ID ' + str(j) , command=lambda k = j:yolov5(k))
    e.grid(row=i, column=j)

# Keep the window open
win.mainloop()

#CameraAdapterEnd

