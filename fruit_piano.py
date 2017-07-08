#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, random
import pygame
import time
from sys import exit
import signal
import Adafruit_MPR121.MPR121 as MPR121


print("""
==============================
  Fruit Piano? FRUIT PIANO!
==============================
""")

# LET THERE BE FEELINGS!
cap = MPR121.MPR121()

# LET THERE BE MUSIC!
pygame.init()
pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.mixer.init()
volume = 1
pygame.mixer.music.set_volume(volume)

if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

print('Press Ctrl-C to quit.')

while True:
    current_touched = cap.touched()
    # Check each pin's last and current state to see if it was pressed or released.
    for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            print(i)

            song = "./sfx/drums/" + str(i) + ".mp3"

            # load the song
            pygame.mixer.music.load(song)

            # play the song
            pygame.mixer.music.play(1)

        # Next check if transitioned from touched to not touched.
        # if not current_touched & pin_bit and last_touched & pin_bit:
        #     print('{0} released!'.format(i))
    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    time.sleep(0.01)