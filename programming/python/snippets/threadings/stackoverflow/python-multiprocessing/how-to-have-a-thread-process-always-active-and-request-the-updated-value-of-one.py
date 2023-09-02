import multiprocessing
from threading import Thread
import time
import random

import numpy as np
import cv2

#function that requests frames
def actions_func(conn):
    try:
        while True:
            time.sleep(random.randint(1,5))
            # Ask for latest frame by sending any message:
            conn.send('frame')
            frame = conn.recv() # This is the response
             cv2.imshow('requested_frame_1',frame)

            time.sleep(random.randint(1,5))
            # Ask for latest frame by sending any message:
            conn.send('frame')
            frame = conn.recv() # This is the response
            cv2.imshow('requested_frame_2',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): break
    except BrokenPipeError:
        # The capture_cam process has terminated.
        pass

def handle_frame_requests(conn):
    try:
        while True:
            # Any message coming in is a request for the latest frame:
            request = conn.recv()
            conn.send(frame) # The frame must be pickle-able
    except EOFError:
        # The actions_func process has ended
        # and its connection has been closed.
        pass

#function that keeps the camera always on and should return the frame value with the last image only when requested
def capture_cam(conn):
    global frame

    frame = None

    # start dameon thread to handle frame requests:
    Thread(target=handle_frame_requests, args=(conn,), daemon=True).start()

    cap = cv2.VideoCapture(1)

    if (cap.isOpened() == False):
        print("Unable to read camera feed")

    # Default resolutions of the frame are obtained. The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))


    while(True):
        ret, frame = cap.read()

        if ret == True:
            cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): break

        else:
            break


def main_process(finish_state):
    conn1, conn2 = multiprocessing.Pipe(duplex=True)

    p1 = multiprocessing.Process(target=capture_cam, args=(conn1,))
    p1.start()

    p2 = multiprocessing.Process(target=actions_func, args=(conn2,))
    p2.start()


if __name__ == '__main__':
    finish_state = multiprocessing.Event()
    main_process(finish_state)