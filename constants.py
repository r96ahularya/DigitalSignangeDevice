from uuid import getnode as get_mac

SERVER = "34.93.136.27"
BACKEND_PORT = "8080"
DOMAIN = "http://"+SERVER+":8080"

MY_DEVICE_ID = str(get_mac())
# MY_DEVICE_ID = "d1"
MY_USER = "bob"
MY_PASSWORD = "bob"
REMOTE_PATH = "/home/"+MY_USER+"/"
LOCAL_PATH = "./"
IMAGE_FORMAT = ".png"
VIDEO_FORMAT = ".mp4"
NOHUP_FORMAT = ".out"
LIVE_CHECK_INTERVAL = 10.0

# Messages
DEFAULT_MESSAGE = "For One stop advertisements, Please contact Bob The Builder Advertising: +91-1231321234"

# Endpoints
POST_REGISTER_ENDPOINT = DOMAIN+"/register"
GET_LIVE_ENDPOINT = DOMAIN+"/device/live/"
GET_PLAYLIST_ENDPOINT = DOMAIN+"/playlist/fetchPlaylist"
GET_FILE_ENDPOINT = DOMAIN+"/storage/downloadFile/"
GET_IMAGE_ID_ENDPOINT = DOMAIN+"/playlist/fetchImageIdsForDevice"
GET_VIDEO_ID_ENDPOINT = DOMAIN+"/playlist/fetchVideoIdsForDevice"
SEND_USAGE_STATISTICS = DOMAIN+"/playlist/updateUsageStats"

# Sample Json to test template 1 -- TEXT
sampleJson1_1 = [{
        "templateId" : 1,
        "startTime" : "22:52:50",
        "durationInSeconds" : 5,
        "centreMiddle" : {
            "contentType" : "text",
            "text" : "Welcome to Bangalore Airport"
        }           
    }]

# Sample Json to test template 1 -- Image
sampleJson1_2 = [{
        "templateId" : 1,
        "startTime" : "22:52:50",
        "durationInSeconds" : 5,
        "centreMiddle" : {
            "contentType" : "image",
            "fileId" : 1
        }           
    }]

sampleJson1_3 = [{
        "templateId" : 1,
        "startTime" : "22:52:50",
        "durationInSeconds" : 5,
        "centreMiddle" : {
            "contentType" : "video",
            "fileId" : 6
        }           
    }]

# Sample Json to test template 3 -- TEXT / IMAGE / IMAGE
sampleJson3 = [{
        "templateId" : 3,
        "startTime" : "22:52:50",
        "durationInSeconds" : 5,
        "topMiddle" : {
            "contentType" : "text",
            "text" : "Welcome to Bangalore Airport"
        },
        "bottomLeft" : {
            "contentType" : "image",
            "fileId" : 1
        },
        "bottomRight" : {
            "contentType" : "image",
            "fileId" : 1
        }
                    
    }]

# Sample Json to test a playlist(template 3, template 1, template 1) 
sampleJson = [{
        "templateId" : 3,
        "startTime" : "22:52:50",
        "durationInSeconds" : 3,
        "topMiddle" : {
            "contentType" : "text",
            "text" : "Welcome to Bangalore Airport"
        },
        "bottomLeft" : {
            "contentType" : "image",
            "fileId" : 4
        },
        "bottomRight" : {
            "contentType" : "image",
            "fileId" : 2
        }
                    
    },
    {
        "templateId" : 1,
        "startTime" : "22:52:50",
        "durationInSeconds" : 3,
        "centreMiddle" : {
            "contentType" : "image",
            "fileId" : 3
        }           
    },
    {
        "templateId" : 1,
        "startTime" : "22:52:50",
        "durationInSeconds" : 5,
        "centreMiddle" : {
            "contentType" : "video",
            "fileId" : 6
        }         
    },
    {
        "templateId" : 1,
        "startTime" : "22:52:50",
        "durationInSeconds" : 2,
        "centreMiddle" : {
            "contentType" : "text",
            "text" : "Temperature is 30°C"
        }           
    }]
