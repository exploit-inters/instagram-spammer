#!/usr/bin/env python3

import pyautogui as pg
import sys
import time
import re
import random

TIME_TO_SLEEP = 10
KEYSTROKE = 'cs'
MOUSE_CLICK_POS = (960, 1020)

# 960, 1020

def putCursor():
    global MOUSE_CLICK_POS
    pg.click(x=MOUSE_CLICK_POS[0], y=MOUSE_CLICK_POS[1], clicks=2, interval=0.5, button='left')
    #  pg.typewrite(list(KEYSTROKE), interval=0.2)

def sendUser(username, number):
    '''
    Will type the @username and press ENTER key
    '''
    putCursor()
    print("Sending user #{} -> @{}".format(number, username))
    for _ in range(30):
        pg.typewrite(['backspace'])
    pg.typewrite('@{}\n\n'.format(username))

def getNames(raw):
    username_pattern = re.compile(r'''title=\"\w+\"\shref=\"/(\w+)/\"''')
    users = username_pattern.findall(raw)
    return users

def updateStatus(index):
    with open('.status', 'w') as status:
        status.write(str(index))

def checkStatus():
    try:
        with open('.status', 'r') as status:
            last_number = int(status.read())
            print("last index:", last_number)
            return last_number
    except:
        return 0

def main(raw_data):
    global TIME_TO_SLEEP
    userlist = sorted(getNames(raw_data))
    print("Fetched {} users, i.e.:".format(len(userlist)))
    print(userlist[:50])
    print("... and goes on ...")

    # Initial wait, time to set things up
    time_wait = 10
    print("Waiting {} seconds, time to set thigs up or cancel the program!"\
          .format(time_wait))
    for i in range(time_wait):
        print("{}..".format(i))
        time.sleep(1)

    print("|> Starting process!")

    last_index = checkStatus()

    # for each user, call the sendUser function
    for user, index in zip(userlist, range(len(userlist))):
        if index > last_index:
            try:
                sendUser(user, index)
                updateStatus(index)
                rand_time = random.randint(TIME_TO_SLEEP-5, TIME_TO_SLEEP + 5)
                print("\tWaiting {} seconds...".format(rand_time))
                time.sleep(rand_time) # DO NOT RUN THE PROGRAM WITHOUT THIS!
            except KeyboardInterrupt:
                print("Exiting program!")
                exit(0)

if __name__ == '__main__':
    # check if correct args were passed
    if len(sys.argv) != 2:
        print("Error: Incorrect number of args passed, read the documentation.")
        exit(1)
    else:
        try:
            with open(sys.argv[1], 'r') as input_file:
                # call main with raw data
                main(input_file.read())
        except Exception as e:
            print("Exception {}, please check your given file.".format(e))
            exit(1)

else:
    # display error msg and exit
    print("Error: This program can only be run as main.")
    exit(1)
