import os
import glob
import subprocess

import kivy
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from kivy.app import App
from kivy.core.text import Label as CoreLabel
from kivy.properties import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# kivy version Requirement
kivy.require('1.9.0')

def yolov5MainCamera(instance, *args):
    subprocess.call('python cameraAdapter.py', cwd='yolov5')


def EsrganUpscale(instance, *args):
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    #FlushTempFrames
    files = glob.glob('Real-ESRGAN-0.3.0/tmp_frames/*')
    for f in files:
        os.remove(f)

    # ExtractVideoFrames
    subprocess.call('ffmpeg -i '+filename+' -qscale:v 1 -qmin 1 -qmax 1 -vsync 0 tmp_frames/frame%08d.png',
                    cwd='Real-ESRGAN-0.3.0')
    #UpscaleVideoFrames
    subprocess.call('python inference_realesrgan_video.py -n Videox4 -i tmp_frames -o out_frames -s 2',
                    cwd='Real-ESRGAN-0.3.0')
    #FlushTempFrames
    files = glob.glob('Real-ESRGAN-0.3.0/tmp_frames/*')
    for f in files:
        os.remove(f)

# Load Design File

# Main App layout class
class MonitorAIApp(App):

        def build(self):
            button1 = Button(text="Detect Objects", size_hint=(0.25, 0.18), pos=(350, 100))
            button1.bind(on_press=partial(yolov5MainCamera, button1))
            button2 = Button(text="Enhance Video", size_hint=(0.25, 0.18), pos=(350, 200))
            button2.bind(on_press=partial(EsrganUpscale, button2))
            boxlayout = BoxLayout()
            boxlayout.add_widget(button1)
            boxlayout.add_widget(button2)
            return boxlayout


# run the App
if __name__ == '__main__':
        MonitorAIApp().run()
