#stone-sissors-paper.py
from microbit import *
import random

tyhja = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

faces = [Image.DIAMOND, Image.SWORD, Image.SQUARE, tyhja]

while True:
    display.show(tyhja)
    
    #Microbit gives a random number between 0 and 2 digits. 
    luku = random.randint(0, 2)
    
    #Press A and then the options are displayed.
    if button_a.is_pressed():
        display.show(faces, loop=False, delay=500)

    #Press B microbit shows your choice   
    if button_b.is_pressed():
        sleep(500)
        display.show(faces[luku])
        sleep(3000)
