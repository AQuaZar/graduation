#!/usr/bin/env python

from time import sleep
from datetime import datetime
import sys
import RPi.GPIO as GPIO
import requests
from mfrc522 import SimpleMFRC522


class Reader:

    in1 = 16
    reader = SimpleMFRC522()
    url = "http://192.168.0.104:8000/access/"

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.output(in1, True)

    def readTag(self):
        print("Ready to read tag")
        id, token = self.reader.read()
        print("ID: %s\nToken: %s" % (id, token))
        return (id, token)

    def requestAccess(self, token):
        headers = {"Authorization": f"Token {token}"}
        r = requests.get(self.url, headers=headers)
        timestamp = datetime.now()
        dt_string = timestamp.strftime("%d/%m/%Y %H:%M:%S")
        print("Date and time =", dt_string)
        return (r.content, r.status_code)

    def authorization(self, statusCode):
        if statusCode == 200:
            GPIO.output(self.in1, False)
            sleep(0.5)
            GPIO.output(self.in1, True)
            return "Authorized"
        else:
            GPIO.output(self.in1, False)
            sleep(0.2)
            GPIO.output(self.in1, True)
            sleep(0.2)
            GPIO.output(self.in1, False)
            sleep(0.2)
            GPIO.output(self.in1, True)
            sleep(0.2)
            GPIO.output(self.in1, False)
            sleep(0.2)
            GPIO.output(self.in1, True)
            return "Access denied"


if __name__ == "__main__":
    rd = Reader()
    try:
        while True:
            id, token = rd.readTag()
            print(token)
            content, statusCode = rd.requestAccess(token)
            print(content)
            print(statusCode)
            print(rd.authorization(statusCode))
            sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
