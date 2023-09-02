from multiprocessing import Process, Manager, Queue
import schedule
import time

def checkBirthdays(accountQueue):
    print('[CheckBirthdays] Initated', time.asctime())
    acc = {
        'email': 'demo@test.com'
    }
    accountProcessing = [] if accountQueue.empty() else list(accountQueue.get())
    accountProcessing.append(acc)
    accountQueue.put(accountProcessing) # ****

def createSchedule(accountQueue):
    # similar to cron, executes at a certain time
    schedule.every(1).seconds.do(checkBirthdays, accountQueue)
    while True:
        schedule.run_pending()
        # check every 60 seconds
        time.sleep(1)

def main():
    # FileNotFoundError: [Errno 2] No such file or directory
    manager = Manager()
    accountQueue = manager.Queue()

    # RuntimeError: Queue objects should only be shared between processes through inheritance
    # accountQueue = Queue()
    schedule = Process(target=createSchedule, args=(accountQueue,)).start()
    manager.join()  # <--------------------------------

if __name__ == '__main__':
    main()
    
    # https://stackoverflow.com/questions/69383902/python-queue-inheritance-issues-with-multiple-processes