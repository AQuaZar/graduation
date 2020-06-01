#!/usr/bin/env python

import RPi.GPIO as GPIO
import requests
import json
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
url = "http://192.168.0.104:8000/api-token-obtain/"

try:
        while(True):
            token = input("Please enter token of admin user \n")
            headers = {'Authorization': f"Token {token}"}
            username = input("Write username of user to generate token \n")
            payload = {"username":f"{username}","password":"NAU12345"}
            r = requests.post(url, headers=headers, data=payload)
            print(r.status_code)
            if r.status_code==200:
                parsed = json.loads(r.content)
                print("Now place RFID card to write token \n")
                reader.write(parsed["token"])
                print("Written \n")
            elif r.status_code==401:
                print("Access to server denied, check correctness of token \n")
            else:
                print("Bad request, make sure that user exists or check corectness of credentials \n")
except KeyboardInterrupt:
    GPIO.cleanup()
