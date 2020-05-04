#! Python 3
# websearch.py is a program to open the web through commandline or clipboard.
import sys
import webbrowser
import pyperclip


if len(sys.argv) > 1:
    # get address from commandline
    address = " ".join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
