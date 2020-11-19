import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()

def get_card():
    try:
        id, text = reader.read()
        sleep(1)
        return id

    except:
        return False

    finally:
        GPIO.cleanup()
