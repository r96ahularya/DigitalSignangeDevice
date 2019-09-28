import threading
import json
import requests
import urllib
import base64
from constants import *
from tkinter import *

#### Send Live check to server after every 10 seconds
def liveCheck():
  requests.get(GET_LIVE_ENDPOINT+MY_DEVICE_ID)
  threading.Timer(LIVE_CHECK_INTERVAL, liveCheck).start()

#### Register this device
def registerDevice():
  requests.post(url = POST_REGISTER_ENDPOINT, data = {'device_id':MY_DEVICE_ID, 'status': "OK"})

#### Get Playlist for a device
def getPlaylist():
  return requests.get(GET_PLAYLIST_ENDPOINT,{'deviceId':MY_DEVICE_ID}).json()

#### Pack a Template 1 {Text / Image}
def packTemplate1(textOrUrl, fileType, root):

    if fileType == "text":
        # Text
        labelfont = ('Helvetica', 95, 'bold')
        simpleTitle = Label(root, text = textOrUrl)
        simpleTitle.config(bg='black', fg='yellow')  
        simpleTitle.config(font=labelfont)     
        simpleTitle.pack(expand=YES, fill=X)
        mainloop()
    elif fileType == "image":
        #Image
        u = urllib.request.urlopen(textOrUrl)
        raw_data = u.read()
        u.close()
        b64_data = base64.encodestring(raw_data)
        # The image (but in the label widget)
        image = PhotoImage(data=b64_data)
        imageLabel = Label(root, image=image)
        imageLabel.config()
        imageLabel.pack()
        mainloop() 

#### Pack a Template 3 {Text, Image, Image}
def packTemplate3(text, URL1, URL2, root):
    
  # Tetx
  labelfont = ('Helvetica', 95, 'bold')
  simpleTitle = Label(root, text = text)
  simpleTitle.config(bg='black', fg='yellow')  
  simpleTitle.config(font=labelfont)     
  simpleTitle.grid(row=0, sticky = W)      

  canvas = Canvas(root, width=1)
  canvas.grid(row=1, sticky=N+E+W+S)
  
  ## Image 1
  u1 = urllib.request.urlopen(URL1)
  raw_data1 = u1.read()
  u1.close()
  b64_data1 = base64.encodestring(raw_data1)
  image1 = PhotoImage(data=b64_data1)
  imageLabel1 = Label(canvas, image=image1, width =700)
  imageLabel1.config()
  imageLabel1.grid(row=0, sticky = W)

  ## Image 2
  u2 = urllib.request.urlopen(URL2)
  raw_data2 = u2.read()
  u2.close()
  b64_data2 = base64.encodestring(raw_data2)
  image2 = PhotoImage(data=b64_data2)
  imageLabel2 = Label(canvas, image=image2, width =700)
  imageLabel2.config()
  imageLabel2.grid(row=0, column=1, sticky = W)
  mainloop()


#### Dynamic Template 5 to load text and image as per loaction
def packTemplate5(text, URL, root):
  ## Text
  labelfont = ('Helvetica', 95, 'bold')
  simpleTitle = Label(root, text = text)
  simpleTitle.config(bg='black', fg='yellow')  
  simpleTitle.config(font=labelfont)     
  simpleTitle.grid(row=0) 

  ## Image
  u = urllib.request.urlopen(URL)
  raw_data = u.read()
  u.close()
  b64_data = base64.encodestring(raw_data)
  image = PhotoImage(data=b64_data)
  imageLabel = Label(root, image=image)
  imageLabel.config()
  imageLabel.grid(row=1)
  mainloop()


#### Launch a GUI app to display all the data.
def populatePlayList():
  listPlaylist = getPlaylist()

  ## Iterate over template list for this device

  # for jsonPlaylist in sampleJson:         # Uncomment to try with sample jsons
  for jsonPlaylist in listPlaylist:
      
      ## Launch a window and set attributes
      root = Tk()
      root.attributes("-fullscreen", True)
      root.configure(background='black')
      root.bind('<Escape>',lambda e: root.destroy())

      templateId = int(jsonPlaylist.get("templateId"))
      durationInSeconds = jsonPlaylist.get("durationInSeconds")
      root.after(durationInSeconds*1000, root.destroy)
      if(templateId == 1):
          print("template 1")
          contentType = jsonPlaylist.get("centreMiddle").get("contentType")
          if contentType == "text":
              text = jsonPlaylist.get("centreMiddle").get("text")
              packTemplate1(text, contentType, root)
          elif contentType == "image":
              centreMiddleFileId = jsonPlaylist.get("centreMiddle").get("fileId")
              url = GET_FILE_ENDPOINT+str(centreMiddleFileId)
              packTemplate1(url, contentType, root)
      elif(templateId == 2):
          ## To be implemented
          packTemplate1("template2", "text", root)
      elif(templateId == 3):
          print("template 3")
          displayText = jsonPlaylist.get("topMiddle").get("text")
          bottomLeftFileId = jsonPlaylist.get("bottomLeft").get("fileId")
          bottomRightFileId = jsonPlaylist.get("bottomRight").get("fileId")
          packTemplate3(displayText, GET_FILE_ENDPOINT+str(bottomLeftFileId), GET_FILE_ENDPOINT+str(bottomRightFileId), root)
      elif(templateId == 4):
          ## To be implemented
          packTemplate1("template 4", "text", root)
      elif(templateId == 5):
          displayText = jsonPlaylist.get("topMiddle").get("text")
          bottomMiddleFileId = jsonPlaylist.get("bottomMiddle").get("fileId")
          packTemplate5(displayText, GET_FILE_ENDPOINT+str(bottomMiddleFileId), root)
  populatePlayList() # replay