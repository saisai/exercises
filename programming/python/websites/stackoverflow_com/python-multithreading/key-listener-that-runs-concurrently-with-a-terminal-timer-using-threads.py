# https://stackoverflow.com/questions/73311958/key-listener-that-runs-concurrently-with-a-terminal-timer-using-threads

import concurrent.futures
import time
import os, threading
import keyboard

run_timer = True
keep_scanning = True

def startTimer(seconds):
    while run_timer:
        for i in range(1, seconds):
            print(i)
            time.sleep(1)
            os.system("clear")

def scanForInput():
    global keep_scanning, run_timer
    try:
        while keep_scanning:
            print(keep_scanning)
            if keyboard.is_pressed('space'):
                keep_scanning = False
                run_timer = False
                return "HIT"
    except Exception as e:
        print(e)

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(startTimer, 4)
    f2 = executor.submit(scanForInput)

