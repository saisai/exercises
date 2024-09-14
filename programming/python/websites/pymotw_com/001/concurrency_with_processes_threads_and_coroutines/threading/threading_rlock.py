import threading

lock = threading.RLock()

print("First try: ", lock.acquire())
print("Seconf try: ", lock.acquire(0))
