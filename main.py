from utilsv2 import *

def boot():
    try:
        #### Start application 
        os.system("nohup python3 LiveCheck.py & > livestatus.out")
        fetchAllImages()
    except: 
        print("Some error occured")
        port = os.popen("""ps -ef | grep LiveCheck | grep -v grep | cut -d " " -f2""").read().split("\n")[0]
        os.popen('kill -9 {}'.format(port))
        test = os.listdir(LOCAL_PATH)
        for item in test:
            if item.endswith(IMAGE_FORMAT) or item.endswith(VIDEO_FORMAT) or item.endswith(NOHUP_FORMAT):
                os.remove(os.path.join(LOCAL_PATH, item))
        boot()

boot()
