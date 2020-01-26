#!/usr/bin/python3

from pynput import keyboard
import sys
import os

debug = False


def printd(text):
    if debug:
        print(text)


class LayoutSwitcher:
    def __init__(self):
        self.layout = 1
        self.layout1_cmd = 'setxkbmap us'
        self.layout2_cmd = 'setxkbmap ru'

    def execute(self, cmd):
        printd('Execute command: ' + cmd)
        os.system(cmd)

    def switch(self):
        if self.layout == 1:
            printd('Switch to layout 2')
            self.execute(self.layout2_cmd)
            self.layout = 2
        else:
            printd('Switch to layout 1')
            self.execute(self.layout1_cmd)
            self.layout = 1


# The key combination to switch layout
key_combination = {keyboard.Key.shift, keyboard.Key.ctrl}

lswitcher = LayoutSwitcher()
pressed_keys = set()

'''
 Logic:
 On any key from key_combination add to pressed_keys
 On any key not from key_combination - clear pressed_keys (cancel switch)
 If released any key not from key_combinations - clear pressed_keys (cancel switch)
 If released any key from key_combinations:
   Check that all other keys form key_combinations is in pressed_keys
   If True: switch layout
   Else: clear pressed_keys (cancel switch)
'''


def on_press(key):
    if key in key_combination:
        printd('Key pressed: ' + str(key))
        pressed_keys.add(key)
    else:
        printd('Clear pressed keys')
        pressed_keys.clear()


def on_release(key):
    if key in key_combination:
        if key_combination == pressed_keys:
            printd('Switch layout')
            lswitcher.switch()
    printd('Clear pressed keys')
    pressed_keys.clear()


def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
