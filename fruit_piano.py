#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
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
pygame.mixer.pre_init(44100, -16, 12, 2048)
pygame.mixer.init()
volume = 1
pygame.mixer.music.set_volume(volume)
source_folder = "synths"
channels = ["drumkit", "percussion", "synths", "farts", "funny", "piano", "animals"]
num_channels = len(channels) - 1
current_channel = 0

# LET DECISIONS HAPPEN!
def change_sounds():
    global current_channel
    next_channel = current_channel + 1

    if(next_channel > num_channels):
        next_channel = 0

    current_channel = next_channel
    print("channel: " + str(current_channel) + " / " + channels[current_channel])


if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    exit(1)

try:

    while True:

        current_touched = cap.touched()

        # Check each pin's last and current state to see if it was pressed or released.
        for i in range(12):

            # Each pin is represented by a bit in the touched value.  A value of 1
            # means the pin is being touched, and 0 means it is not being touched.
            pin_bit = 1 << i

            # First check if transitioned from not touched to touched.
            if current_touched & pin_bit and not last_touched & pin_bit:

                if(i == 11):

                    change_sounds()

                else:

                    source_folder = channels[current_channel]
                    print("Sample: " + str(i))
                    song = "/home/pi/fruit_piano/sfx/" + source_folder + "/" + str(i) + ".ogg"

                    sound = pygame.mixer.Sound(song)
                    sound.play(0)

        # Update last state and wait a short period before repeating.
        last_touched = current_touched

except KeyboardInterrupt:
    # kill the piano if the user hits ctrl+c
    print("""
==============================
FRUIT PIANO! OUT!
==============================
    """)
