#!/usr/bin/env python3
import os
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()

while True:
    try:
        id, text = reader.read()
        # print(id)
        os.system("clear")
        print(text)
        sleep(1)

    finally:
        GPIO.cleanup()
