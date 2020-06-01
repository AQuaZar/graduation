#!/usr/bin/env python

from time import sleep
import sys
import RPi.GPIO as GPIO
import requests
from mfrc522 import SimpleMFRC522

in1 = 16
reader = SimpleMFRC522()
url = "http://192.168.0.104:8000/access/"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.output(in1, True)

try:
    while True:
        print("Ready to read tag")
        id, token = reader.read()
        print("ID: %s\nToken: %s" % (id,token))
        headers = {'Authorization': f'Token {token}'}
        r = requests.get(url, headers=headers)
        print(r.content)
        print(r.status_code)
        if r.status_code==200:
            GPIO.output(in1, False)
            sleep(0.5)
            GPIO.output(in1, True)
        else:
            print("Access denied")
            GPIO.output(in1, False)
            sleep(0.2)
            GPIO.output(in1, True)
            sleep(0.2)
            GPIO.output(in1, False)
            sleep(0.2)
            GPIO.output(in1, True)
            sleep(0.2)
            GPIO.output(in1, False)
            sleep(0.2)
            GPIO.output(in1, True)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
     
