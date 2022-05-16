from multiprocessing import Process, Pipe
from threading import Thread

def inputter(input_conn):
    """ get requests to do input calls """
    while True:
        input_msg = input_conn.recv()
        value = input(input_msg)
        input_conn.send(value) # send inputted value:


def worker(msg_conn, input_conn):
    while True:
        message = msg_conn.recv()
        if message is None:
            break
        if message == 'do input':
            # send inputter our prompt message:
            input_conn.send('Enter x: ')
            # get back the result of the input:
            x = (int)(input_conn.recv())
            print('The value entered was', x)
        else:
            print('Got message:', message)


if __name__ == '__main__':
    import time

    # create the connections for sending messages from one process to another:
    recv_conn, send_conn = Pipe(duplex=False)

    # create the connections for doing the input requests:
    input_conn1, input_conn2 = Pipe(duplex=True) # each connection is bi-drectional

    # start the inputter thread with one of the inputter duplex connections:
    t = Thread(target=inputter, args=(input_conn1,), daemon=True)
    t.start()

    # start a child process with the message connection in lieu of a Queue
    # and the other inputter connection:
    p = Process(target=worker, args=(recv_conn, input_conn2))
    p.start()

    # send messages to worker process:
    send_conn.send('a')
    send_conn.send('do input')
    send_conn.send('b')
    # signal the child process to terminate:
    send_conn.send(None)
    p.join()
    
    # https://stackoverflow.com/questions/69632578/python-multiprocessing-read-input-from-child-process