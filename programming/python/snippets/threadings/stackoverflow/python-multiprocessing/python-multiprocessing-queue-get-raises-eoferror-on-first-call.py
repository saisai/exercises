import multiprocessing as mp

def reader(queue):
    while (data := queue.get()) != 'stop':
        print(data)

def main():
    queue = mp.Manager().Queue()
    p = mp.Process(target=reader, args=(queue,))
    p.start()
    for some_data in ['Hello', 'World', 'stop']:
        queue.put(some_data)
    p.join()

if __name__ == '__main__':
    main()

    # https://stackoverflow.com/questions/71175795/python-multiprocessing-queue-get-raises-eoferror-on-first-call