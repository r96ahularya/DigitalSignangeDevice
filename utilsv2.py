import threading
import json
import requests
import urllib
import base64
from StreamVideo import *
from io import BytesIO
from constants import *
from DownloadContent import *
from tkinter import *
from PIL import ImageTk, Image

#### Send Live check to server after every 10 seconds
def liveCheck():
    requests.get(GET_LIVE_ENDPOINT+MY_DEVICE_ID)
    threading.Timer(LIVE_CHECK_INTERVAL, liveCheck).start()

#### Send Usage Statistics to server 
def sendUsageStats():
    requests.get(SEND_USAGE_STATISTICS,{'deviceId':MY_DEVICE_ID})

#### Register this device
def registerDevice():
    requests.post(url = POST_REGISTER_ENDPOINT, data = {'device_id':MY_DEVICE_ID, 'status': "OK"})

#### Get Playlist for a device
def getPlaylist():
    return requests.get(GET_PLAYLIST_ENDPOINT,{'deviceId':MY_DEVICE_ID}).json()

#### Get Image Id for a device
def getImageIds():
    return requests.get(GET_IMAGE_ID_ENDPOINT,{'deviceId':MY_DEVICE_ID}).json()

#### Get Video Id for a device
def getVideoIds():
    return requests.get(GET_VIDEO_ID_ENDPOINT,{'deviceId':MY_DEVICE_ID}).json()

def fetchAllVideos():
    print("Starting video downloads")
    contentIdList = getVideoIds()
    if len(contentIdList) == 0:
        populatePlayListv2()
    else:
        contentIdList = list(map(str, contentIdList))
        print(contentIdList)
        for fileId in contentIdList:
            if not os.path.exists(fileId+VIDEO_FORMAT):
                downloadeFile(fileId, "video")
                print(fileId+" downloaded successfully!!")
        print("All videos downloaded successfully!!")
        populatePlayListv2()

def fetchAllImages():
    print("Starting image downloads")
    contentIdList = getImageIds()
    if len(contentIdList) == 0:
        fetchAllVideos()
    else:
        contentIdList = list(map(str, contentIdList))
        print(contentIdList)
        for fileId in contentIdList:
            if not os.path.exists(fileId+IMAGE_FORMAT):
                downloadeFile(fileId, "image")
                print(fileId+" downloaded successfully!!")
        print("All images downloaded successfully!!")
        fetchAllVideos()

#### Pack a Template 1 {Text / Image}
def packTemplate1(textOrFileId, fileType, root):

    if fileType == "text":
        # Text
        labelfont = ('Helvetica', 95, 'bold')
        simpleTitle = Label(root, text = textOrFileId, wraplength = root.winfo_screenwidth()-20)
        simpleTitle.config(bg='black', fg='yellow')  
        simpleTitle.config(font=labelfont)     
        simpleTitle.pack(expand=YES, fill=X)
        root.mainloop()
    elif fileType == "image":
        #Image
        image = ImageTk.PhotoImage(Image.open(textOrFileId+IMAGE_FORMAT).resize((root.winfo_screenwidth(),root.winfo_screenheight())))
        imageLabel = Label(root, image=image)
        imageLabel.config(bg = 'black')
        imageLabel.pack(fill=BOTH, expand = YES)
        root.mainloop() 
    elif fileType == "video":
        playVideo(textOrFileId, root)
        # root.destroy()

#### Pack a Template 3 {Text, Image, Image}
def packTemplate3(text, fileId1, fileId2, root):
    
    # Text
    labelfont = ('Helvetica', 95, 'bold')
    simpleTitle = Label(root, text = text, wraplength = root.winfo_screenwidth()-20)
    simpleTitle.config(bg='black', fg='yellow')  
    simpleTitle.config(font=labelfont)     
    simpleTitle.grid(row=0)      

    canvas = Canvas(root, bg='black')
    canvas.grid(row=1)
    
    ## Image 1
    image1 = ImageTk.PhotoImage(Image.open(fileId1+IMAGE_FORMAT).resize((int(root.winfo_screenwidth()/2),root.winfo_screenheight()-int(0.132*root.winfo_screenheight()))))
    imageLabel1 = Label(canvas, image=image1)
    imageLabel1.config()
    imageLabel1.grid(row=0)

    ## Image 2
    image2 = ImageTk.PhotoImage(Image.open(fileId2+IMAGE_FORMAT).resize((int(root.winfo_screenwidth()/2),root.winfo_screenheight()-int(0.132*root.winfo_screenheight()))))
    imageLabel2 = Label(canvas, image=image2)
    imageLabel2.config()
    imageLabel2.grid(row=0, column=1)
    root.mainloop()


#### Dynamic Template 5 to load text and image as per loaction
def packTemplate5(text, URL, root):
    ## Text
    labelfont = ('Helvetica', 95, 'bold')
    simpleTitle = Label(root, text = text, wraplength = root.winfo_screenwidth()-20)
    simpleTitle.config(bg='black', fg='yellow')  
    simpleTitle.config(font=labelfont)     
    simpleTitle.grid(row=0) 

    ## Image
    u = urllib.request.urlopen(URL)
    raw_data = u.read()
    u.close()
    image = ImageTk.PhotoImage(Image.open(BytesIO(raw_data)).resize((int(root.winfo_screenwidth()),root.winfo_screenheight()-int(0.132*root.winfo_screenheight()))))
    imageLabel = Label(root, image=image)
    imageLabel.config()
    imageLabel.grid(row=1)
    root.mainloop()

#### Launch a GUI app to display all the data.
def populatePlayListv2():
    listPlaylist = getPlaylist()

    if len(listPlaylist) == 0:
        root = Tk()
        root.attributes("-fullscreen", True)
        root.configure(background='black')
        root.bind('<Escape>',lambda e: root.destroy())
        root.after(2000, root.destroy)
        packTemplate1(DEFAULT_MESSAGE, "text", root)
        populatePlayListv2()
    else:

        ## Iterate over template list for this device
        # for jsonPlaylist in sampleJson:         # Uncomment to try with sample jsons
        for jsonPlaylist in listPlaylist:         # Uncomment to try with actual jsons
            ## Launch a window and set attributes
            root = Tk()
            root.attributes("-fullscreen", True)
            root.configure(background='black')
            root.bind('<Escape>',lambda e: root.destroy())

            templateId = int(jsonPlaylist.get("templateId"))
            durationInSeconds = int(jsonPlaylist.get("durationInSeconds"))

            if(templateId == 1):
                print("template 1")
                contentType = jsonPlaylist.get("centreMiddle").get("contentType")
                if contentType == "text":
                    root.after(durationInSeconds*1000, root.destroy)
                    text = jsonPlaylist.get("centreMiddle").get("text")
                    packTemplate1(text, contentType, root)
                elif contentType == "image":
                    root.after(durationInSeconds*1000, root.destroy)
                    centreMiddleFileId = jsonPlaylist.get("centreMiddle").get("fileId")
                    packTemplate1(str(centreMiddleFileId), contentType, root)
                elif contentType == "video":
                    centreMiddleFileId = jsonPlaylist.get("centreMiddle").get("fileId")
                    packTemplate1(str(centreMiddleFileId), contentType, root)
            elif(templateId == 2):
                ## To be implemented
                packTemplate1("template2", "text", root)
            elif(templateId == 3):
                print("template 3")
                root.after(durationInSeconds*1000, root.destroy)
                displayText = jsonPlaylist.get("topMiddle").get("text")
                bottomLeftFileId = jsonPlaylist.get("bottomLeft").get("fileId")
                bottomRightFileId = jsonPlaylist.get("bottomRight").get("fileId")
                packTemplate3(displayText, str(bottomLeftFileId), str(bottomRightFileId), root)
            elif(templateId == 4):
                ## To be implemented
                print("template 4")
                packTemplate1("template 4", "text", root)
            elif(templateId == 5):
                print("template 5")
                root.after(durationInSeconds*1000, root.destroy)
                displayText = jsonPlaylist.get("topMiddle").get("text")
                bottomMiddleFileId = jsonPlaylist.get("bottomMiddle").get("fileId")
                packTemplate5(displayText, GET_FILE_ENDPOINT+str(bottomMiddleFileId), root)
        sendUsageStats() # send content usage statistics
        fetchAllImages() # replay
