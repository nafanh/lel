#! python3
#Launches a map in the browser using
# address from the comman lind

import webbrowser, sys, pyperclip
if len(sys.argv) < 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
