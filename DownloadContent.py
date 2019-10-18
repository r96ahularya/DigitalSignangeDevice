import os
import sys
import csv
import pysftp
from constants import *


def downloadeFile(fileId, contentType):
    FORMAT = ""
    if contentType == "image":
        FORMAT = IMAGE_FORMAT
    elif contentType == "video":
        FORMAT = VIDEO_FORMAT

    try:
        s = pysftp.Connection(SERVER, username=MY_USER, password=MY_PASSWORD)
        remotepath = REMOTE_PATH+fileId+FORMAT
        localpath = "./"+fileId+FORMAT
        s.get(remotepath, localpath)
        s.close()
    except Exception:
        print("Content downloading failed")
