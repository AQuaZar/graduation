#!/usr/bin/env python

import RPi.GPIO as GPIO
import requests
import json
from mfrc522 import SimpleMFRC522


class Writer:
    reader = SimpleMFRC522()
    url = "http://192.168.0.104:8000/api-token-obtain/"

    def requestToken(self, token, username):
        headers = {'Authorization': f"Token {token}"}
        payload = {"username":f"{username}","password":"NAU12345"}
        r = requests.post(self.url, headers=headers, data=payload)
        return (r.status_code, r.content)
    
    def writeTokenOnTag(self, statusCode, content):
        if statusCode==200:
            parsed = json.loads(content)
            print("Please, place RFID card to write token. \n")
            self.reader.write(parsed["token"])
            return("Success! Data has been written. \n")
        elif statusCode==401:
            return("Access to server denied, check correctness of token. \n")
        else:
            return("Bad request, make sure that user exists or check correctness of credentials. \n")


if __name__ == "__main__":
    wr = Writer()
    try:
        while True:
            token = input("Please, enter token of admin user \n")
            username = input("Write username whose token has to be generated \n")
            statusCode, content = wr.requestToken(token, username)
            print(wr.writeTokenOnTag(statusCode, content))

    except KeyboardInterrupt:
        GPIO.cleanup()
