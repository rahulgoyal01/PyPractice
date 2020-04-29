import webbrowser, sys, pyperclip

#sys.argv is used to get system aruments for address using batch file

sys.argv # ['mapit.py', 'C-62', 'Duggal Colony', 'Khanpur']

#Check if CLI arguments are passed

if len(sys.argv) > 1:
    # ['mapit.py', 'C-62', 'Duggal Colony', 'Khanpur'] --> 'C-62 Duggal Colony Khanpur'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#https://www.google.com/maps/search/<ADDRESS>

webbrowser.open('https://www.google.com/maps/search/' + address)

# mapit.bat created in the same directory as for
# this file, however this need to be copied in user
# directory in C drive so that mapit can run directly
# using W+R(run) and adding address after it
