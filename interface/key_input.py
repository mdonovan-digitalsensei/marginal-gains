import curses
import sys,os


def key_input(thekey, marvin):
    if thekey == "KEY_DOWN":
        marvin.move(1, 0)
    elif thekey == "KEY_UP":
        marvin.move(-1, 0)
    elif thekey == "KEY_LEFT":
        marvin.move(0, -1)
    elif thekey == "KEY_RIGHT":
        marvin.move(0, 1)
