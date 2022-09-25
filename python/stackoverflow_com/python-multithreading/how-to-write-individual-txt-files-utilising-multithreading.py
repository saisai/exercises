
import threading

def writeToFile(fileNumber):
    with open(f'File{fileNumber}.txt', 'w') as file:
        for i in range(5):
            print(f"WroteToFile: {fileNumber}")
            file.write("hello\n")

thread_list = []

thread_list.append(threading.Thread(target=writeToFile, args=[0]))
thread_list.append(threading.Thread(target=writeToFile, args=[1]))

# start the threads
for index, thread in enumerate(thread_list):

    thread.start()
    print(f"ThreadNumber {index} started")

# wait unitl all thread are terminated
for thread in thread_list:
    thread.join()

# https://stackoverflow.com/questions/73812963/how-to-write-individual-txt-files-utilising-multithreading
