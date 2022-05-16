import os
import subprocess
import multiprocessing

'''
def worker(w_conn):
    os.dup2(w_conn.fileno(), 2)
    sp = subprocess.Popen(['python', 'hello.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    #sp = subprocess.Popen(['java', 'myprogram'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    sp.wait()
    w_conn.close()
'''
def worker(w_conn):
    sp = subprocess.Popen(['python', 'hello.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sp.wait()
    if sp.stderr.seek(0, io.SEEK_END)>0:
        w_conn.send(sp.stderr.read())
    w_conn.close()

def main():
    r_conn, w_conn = multiprocessing.Pipe(False)
    process = multiprocessing.Process(target=worker, args=(w_conn,))
    process.start()
    
    while not r_conn.poll() and not w_conn.closed:
        # Do stuff
        print("do stuff")
        break
    else:
        # Read error from r_conn, and handle it
        print("error")
    
    r_conn.close()
    process.join()

if __name__=='__main__':
    main()
    
    # https://stackoverflow.com/questions/69415087/python-multiprocessing-pipe-and-redirecting-stderr-on-windows