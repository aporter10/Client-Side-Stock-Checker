from pyautogui import *
import pyautogui
import time
import pyautogui as ptg
from playsound import playsound
from twilio.rest import Client


client = Client("","")  # add client number for twillo



while True:
    if pyautogui.locateOnScreen(os.path.join('imgs', 'addtocart.jpg'), confidence=0.8) != None:
        playsound(os.path.join('sounds', 'Alarm.mp3'))
        client.messages.create(to="", from_="", body="Check Cart Now")
        break
    else:
        ptg.hotkey('ctrl', 'r')
        time.sleep(30.0)
