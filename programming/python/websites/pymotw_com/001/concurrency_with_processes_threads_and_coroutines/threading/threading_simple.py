import threading


def worker():
    """Thread worker function"""
    print("Worker")

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

