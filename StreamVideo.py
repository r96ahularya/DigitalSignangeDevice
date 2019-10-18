import urllib
import requests

import imageio
from constants import *
from tkinter import *
from PIL import ImageTk, Image
from moviepy.editor import VideoFileClip
def stream(label, video, delay, root):
  
    try:
      image = video.get_next_data()
    except:
      video.close()
      return
    label.after(delay, lambda: stream(label, video, delay, root))
    frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize((root.winfo_screenwidth(),root.winfo_screenheight())))
    label.config(image=frame_image)
    label.image = frame_image

def playVideo(fileId, root):

    #link of the video to be downloaded 
    video_name = "./"+fileId+VIDEO_FORMAT
    video = imageio.get_reader(video_name)
    delay = int(1000 / video.get_meta_data()['fps'])
    my_label = Label(root)
    my_label.grid(row=0)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    my_label.after(delay, lambda: stream(my_label, video, delay, root))
    root.after(int((VideoFileClip(fileId+VIDEO_FORMAT).duration)*1000), root.destroy)
    root.mainloop()
