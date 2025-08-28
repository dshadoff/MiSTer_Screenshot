# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MiSTer-specific screen capture usage by Dave Shadoff

"""CircuitPython Essentials HID Keyboard example"""
import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# A simple neat keyboard demo in CircuitPython

# The pins we'll use, each will have an internal pullup
keys_pressed = [1, 2]
keypress_pins = [board.TIP,board.RING_1]

# Our array of built key objects
key_pin_array = []

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# set the sleeve to ground
ground_pin = digitalio.DigitalInOut(board.SLEEVE)
ground_pin.direction = digitalio.Direction.OUTPUT
ground_pin.value = False

# Make all other pin objects inputs with pullups
for pin in keypress_pins:
    key_pin = digitalio.DigitalInOut(pin)
    key_pin.direction = digitalio.Direction.INPUT
    key_pin.pull = digitalio.Pull.UP
    key_pin_array.append(key_pin)   # Add to array of key objects

while True:
    for key_pin in key_pin_array:
        if not key_pin.value:  # Is it grounded?
            i = key_pin_array.index(key_pin)
#            print("Pin #%d is grounded." % i)
            while not key_pin.value:
                pass  # Wait for it to be ungrounded!
            key = keys_pressed[i]  # Get the corresponding Key

            if key == 1:   # Tip, or "B" on 8BitDo buttons
                keyboard.press(Keycode.GUI, Keycode.SHIFT, Keycode.PRINT_SCREEN)  # "Press"...
                keyboard.release_all()  # ..."Release"!

            if key == 2:   # Ring_1, or "A" on 8BitDo buttons
                keyboard.press(Keycode.GUI, Keycode.PRINT_SCREEN)  # "Press"...
                keyboard.release_all()  # ..."Release"!

    time.sleep(0.01)
