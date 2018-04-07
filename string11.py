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

cap = cv2.VideoCapture(0)

ret, image = cap.read()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "input.png"
cv2.imwrite("input.png", gray)
print ("works")
text = pytesseract.image_to_string(gray)
#os.remove(filename)

print (text)


if "WATCH" in text or "OUT" in text:
	os.system("gtts-cli.py -f 1.txt -l 'hi' -o outAudio.mp3")
	print ("DONE")
elif "drive" in text or "slow" in text:
	os.system("gtts-cli.py -f 2.txt -l 'hi' -o outAudio.mp3")
	print ("DONE")
elif "DANGER" in text or "work" in text:
	os.system("gtts-cli.py -f 3.txt -l 'hi' -o outAudio.mp3")
	print ("DONE")
else:
	translated_lines = gs.translate(text,'hi')
	print(translated_lines, file=open("goslate.txt", "a"))
	os.system("gtts-cli.py -f goslate.txt -l 'hi' -o outAudio.mp3")
	print ("Go DONE")

os.system("omxplayer outAudio.mp3")

cap.release()
cv2.destroyAllWindows()