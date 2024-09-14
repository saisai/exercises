from threading import Thread, Event
import time

def countdown(n, started_evt):
    print("countdown starting")
    started_evt.set()
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)

started_evt = Event()


print("Launching countdown")
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# Wait for the thread to start
started_evt.wait()
print("Countdown is running")

