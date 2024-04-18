#Import packages
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import urllib.request
from IPython.display import Video
from pytube import YouTube


#Downloading video
yt = pytube.YouTube('https://www.youtube.com/watch?v=i0a61wFaF8A')
url = 'https://www.youtube.com/watch?v=i0a61wFaF8A'
vid = YouTube(url)
yt = vid.streams.first().download()
yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()

# Displaying the video
Video('video.mp4', width=550, start=30, end=40)
