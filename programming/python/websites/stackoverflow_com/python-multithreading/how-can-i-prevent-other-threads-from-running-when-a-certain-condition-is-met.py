'''
https://stackoverflow.com/questions/73396086/how-can-i-prevent-other-threads-from-running-when-a-certain-condition-is-met/73474910#73474910

'''
import threading, string, random, time

def anotherThread(is_printing_alphabet: threading.Event):
    this_thread = threading.current_thread().name

    print(f"Running {this_thread}...")

    i = 0

    while i < 10:
        while not is_printing_alphabet.is_set():
            print(f"Processing {i} from {this_thread}....")
            time.sleep(1) # processing here
            i += 1
    print(f"Running {this_thread}... Done")


def printAlphabet(is_printing_alphabet: threading.Event):

    print("Printing Alphabet! All threads stop!")
    is_printing_alphabet.set()
    for letter in string.ascii_lowercase:
        print(str(letter))
        time.sleep(0.01)
    print('All threads may resume...')
    is_printing_alphabet.clear()

def main():
    is_printing_alphabet = threading.Event()

    threads = [
            threading.Thread(target=anotherThread, daemon=True, args=(is_printing_alphabet,)),
            threading.Thread(target=anotherThread, daemon=True, args=(is_printing_alphabet,)),
            ]
    for thread in threads:
        thread.start()
    time.sleep(2)

    print_alphabet = threading.Thread(target=printAlphabet, args=(is_printing_alphabet,))
    print_alphabet.start()

    print_alphabet.join()

    time.sleep(5)

    for thread in threads:
        thread.join()

main()

