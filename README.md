# SignangeDevice
It is an application which communicates with the server to display the advertisemet in the form of a digital signange board.

## Working:
1. Device Status:
The device needs to be registererd with the server with a unique deviceId. It which can be seen in MY_DEVICE_ID in constants.py. After successful registration, the Signage Device will continuously send the status of this device to the server. The duration can be configured at LIVE_CHECK_INTERVAL in constants.py

2. Running the application 
Since the device is successfully registered with the server, the application will fetch a playlist which is configured in DB for this device. The playlist json is then iterated based on the screen co-ordinate(top left, bottom right etc). The json holds a list of templates which together is known as a playlist (json). These templates hold a templateId for which they are packed (processed and displayed). Now as per the playlist the application starts displaying the content whose information is sent in received from the json in populatePlayList() in utils.py.

This application uses tkinter for serving the purpose of GUI as python with tkinter outputs the fastest and easiest way to create the GUI applications.

Sample Jsons can be taken from constants.py

## Pre-requisites for running the appliaction
1. Python3
2. Pip3
3. requests library (```sudo pip3 install requests```)
4. imageio library (```sudo pip3 install imageio```)
5. Pillow library (```sudo pip3 install Pillow```)
6. moviepy library (```sudo pip3 install moviepy```)
7. Domain set in constants.py under "DOMAIN"

## How to run
Launch 2 terminal instances
1. For sending the live status of this device 
    ```bash 
    python3 liveChek.py
    ```

2. For running the application
    ```bash 
    python3 main.py
    ```

The appliccation will collect the playlist (list of templates) and its corresponding data(fileId/text) and populate it in the GUI.
* File Id (fileId) is the unique Id with which an image is stored in the DB
