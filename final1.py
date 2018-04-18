from PIL import Image
from string import Template
import numpy as np
import pytesseract
import cv2
import os
from gtts import gTTS
import goslate
gs = goslate.Goslate()

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(28, GPIO.IN)
GPIO.setup(29, GPIO.IN)


cap = cv2.VideoCapture(0)


while True:

    ret, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = "input.png"
    cv2.imwrite("input.png", gray)
    text = pytesseract.image_to_string(gray)

    language = {'hindi': 0, 'bengali': 0, 'tamil': 0}

    if GPIO.input(25):
        language['hindi'] = 1
        
    if GPIO.input(26):
        language['bengali'] = 1
       
    if GPIO.input(27):
        language['tamil'] = 1

    if GPIO.input(29): 
        cap.release()
        cv2.destroyAllWindows()
        print("Exited")
        break

    
    if language['hindi']:
        if "WATCH" in text or "OUT" in text:
            os.system("gtts-cli.py -f 1.txt -l 'hi' -o outAudio.mp3")
            print("DONE")
        elif "drive" in text or "slow" in text:
            os.system("gtts-cli.py -f 2.txt -l 'hi' -o outAudio.mp3")
            print("DONE")
        elif "DANGER" in text or "work" in text:
            os.system("gtts-cli.py -f 3.txt -l 'hi' -o outAudio.mp3")
            print("DONE")
        else:
            print("Camera Unavailable")

        os.system("omxplayer outAudio.mp3")

    elif language['bengali']:
        if "WATCH" in text or "OUT" in text:
            os.system("gtts-cli.py -f 11.txt -l 'bn' -o outAudio.mp3")
            print("DONE")
        elif "drive" in text or "slow" in text:
            os.system("gtts-cli.py -f 22.txt -l 'bn' -o outAudio.mp3")
            print("DONE")
        elif "DANGER" in text or "work" in text:
            os.system("gtts-cli.py -f 33.txt -l 'bn' -o outAudio.mp3")
            print("DONE")
        else:
            print("Camera Unavailable")

        os.system("omxplayer outAudio.mp3")

    elif language['tamil']:
        if "WATCH" in text or "OUT" in text:
            os.system("gtts-cli.py -f 111.txt -l 'ta' -o outAudio.mp3")
            print("DONE")
        elif "drive" in text or "slow" in text:
            os.system("gtts-cli.py -f 222.txt -l 'ta' -o outAudio.mp3")
            print("DONE")
        elif "DANGER" in text or "work" in text:
            os.system("gtts-cli.py -f 333.txt -l 'ta' -o outAudio.mp3")
            print("DONE")
        else:
           print("Camera Unavailable")

        os.system("omxplayer outAudio.mp3")

    sleep(5)
    #delay of 5 second
