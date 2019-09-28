from uuid import getnode as get_mac

DOMAIN = "http://192.168.225.208:8081"
MY_DEVICE_ID = str(get_mac())
LIVE_CHECK_INTERVAL = 10.0

# Endpoints
POST_REGISTER_ENDPOINT = DOMAIN+"/register"
GET_LIVE_ENDPOINT = DOMAIN+"/device/live/"
GET_PLAYLIST_ENDPOINT = DOMAIN+"/playlist/fetchPlaylist"
GET_FILE_ENDPOINT = DOMAIN+"/storage/downloadFile/"

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
            "fileId" : 50
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
            "fileId" : 13
        },
        "bottomRight" : {
            "contentType" : "image",
            "fileId" : 9
        }
                    
    }]

# Sample Json to test a playlist(template 3, template 1, template 1) 
sampleJson = [{
        "templateId" : 3,
        "startTime" : "22:52:50",
        "durationInSeconds" : 5,
        "topMiddle" : {
            "contentType" : "text",
            "text" : "Welcome to Bangalore Airport"
        },
        "bottomLeft" : {
            "contentType" : "image",
            "fileId" : 10
        },
        "bottomRight" : {
            "contentType" : "image",
            "fileId" : 9
        }
                    
    },
    {
        "templateId" : 1,
        "startTime" : "22:52:50",
        "durationInSeconds" : 3,
        "centreMiddle" : {
            "contentType" : "image",
            "fileId" : 16
        }           
    },
    {
        "templateId" : 1,
        "startTime" : "22:52:50",
        "durationInSeconds" : 10,
        "centreMiddle" : {
            "contentType" : "text",
            "text" : "Temperature is 30°C"
        }           
    }]