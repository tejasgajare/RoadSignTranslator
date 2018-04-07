from PIL import Image
from string import Template
import numpy as np
import pytesseract
import cv2
import os
from gtts import gTTS
import goslate
import time
gs = goslate.Goslate()

import RPi.GPIO as GPIO  
from time import sleep    
GPIO.setmode(GPIO.BCM)     
GPIO.setup(25, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(28, GPIO.IN)

GPIO.output(25, 0)
GPIO.output(26, 0)
GPIO.output(27, 0)
GPIO.output(28, 0)


cap = cv2.VideoCapture(0)

ret, image = cap.read()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "input.png"
cv2.imwrite("input.png", gray)
print("works")
text = pytesseract.image_to_string(gray)
#os.remove(filename)

flag = 0
while True:             
        if GPIO.input(25):
       		flag = 1
       		break
       	if GPIO.input(26):
       		flag = 2
       		break
       	if GPIO.input(27):
       		flag = 3
       		break

if flag == 1 :
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
		translated_lines = gs.translate(text,'hi')
		print(translated_lines, file=open("goslate1.txt", "a"))
		os.system("gtts-cli.py -f goslate1.txt -l 'hi' -o outAudio.mp3")
		print("Go DONE")

	os.system("omxplayer outAudio.mp3")
	flag = 0

elif flag == 2 :
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
		translated_lines = gs.translate(text,'bn')
		print(translated_lines, file=open("goslate2.txt", "a"))
		os.system("gtts-cli.py -f goslate2.txt -l 'bn' -o outAudio.mp3")
		print("Go DONE")

	os.system("omxplayer outAudio.mp3")
	flag = 0

elif flag == 3 :

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
		translated_lines = gs.translate(text,'ta')
		print(translated_lines, file=open("goslate3.txt", "a"))
		os.system("gtts-cli.py -f goslate3.txt -l 'ta' -o outAudio.mp3")
		print("Go DONE")

	os.system("omxplayer outAudio.mp3")
	flag = 0
