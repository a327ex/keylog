import keyboard
import timer
import sys
import datetime
from copy import copy
from time import sleep
from threading import Timer

count = 0

def onKeyUp(event):
    global count 
    count = count + 1

def storeCounts():
    while True:
        global count
        now = datetime.datetime.now()
        countfile = open("C:/Users/gen/Desktop/dev/keylog/logs/" + str(now.day) + '-' + str(now.month) + '-' + str(now.year) + "_" + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second), "w")
        countfile.write(str(count))
        countfile.close()
        count = 0
        sleep(3600.0)

captureThread = Timer(3600.0, storeCounts)
captureThread.start()

keyboard.on_release(onKeyUp)
keyboard.wait()
