#!/usr/bin/env python3

import pyautogui as pg
import pandas as pd
import os
import sys
import time
import re
import random

TIME_TO_SLEEP = 10

def putCursor(click_pos):
    pg.click(x=click_pos[0], y=click_pos[1], clicks=2, interval=0.3, button='left')

def sendUser(username, number, click_pos):
    '''
    Will type the @username and press ENTER key, then reload the page
    '''
    putCursor(click_pos)
    print("Typing user #{} ~ @{}".format(number, username))
    pg.typewrite('@{}\n'.format(username))
    time.sleep(2)
    pg.typewrite(['f5']) # reload page

def getNames():
    '''
    Will create a dataframe object with pandas from the .csv created with
    'Helper Tools for Instagram', and filter only the usernames
    '''
    files = [ file.name for file in os.scandir('assets/') if file.name[-4:] == '.csv' ]
    valid_users = list()
    for file in files:
        df = pd.read_csv('assets/' + file)

        # catch all usernames from the file
        [ valid_users.append(person) for person in list(df['username']) ]

    return list(set(valid_users))

def updateStatus(index):
    '''
    Will update .status file with the current index being sent to instagram
    '''
    with open('.status', 'w') as status:
        status.write(str(index))

def checkStatus():
    '''
    Will read .status to know in which index the program has stopped earlier
    '''
    try:
        with open('.status', 'r') as status:
            last_number = int(status.read())
            print("Resuming from: #", last_number)
            return last_number
    except:
        return 0

def main():
    ''' main function '''
    global TIME_TO_SLEEP

    userlist = sorted(getNames())
    print("@INFO: Fetched {} users".format(len(userlist)))

    try:
        input("Please, hit enter when positioned the mouse on the correct spot...")
        mouse_pos = pg.position()
        print("Captured position:", mouse_pos)
        print("Starting spammer!")

    except KeyboardInterrupt:
        print("\n\nNevermind")
        exit()

    print("-"*80)
    last_index = checkStatus()

    # for each user, call the sendUser function
    for user, index in zip(userlist, range(len(userlist))):
        if index > last_index:
            try:
                sendUser(user, index, mouse_pos)
                updateStatus(index)
                rand_time = random.randint(TIME_TO_SLEEP-5, TIME_TO_SLEEP + 5)
                print("\tWait: {}s".format(rand_time))
                time.sleep(rand_time) # DO NOT RUN THE PROGRAM WITHOUT THIS!
                #  time.sleep(1)
            except KeyboardInterrupt:
                print("-"*80)
                print("Exiting program!")
                exit(0)
    print("-"*80)
    print("Finished all {} users".format(len(userlist)))

if __name__ == '__main__':
    main()
else:
    # display error msg and exit
    print("Error: This program can only be run as main.")
    exit(1)
