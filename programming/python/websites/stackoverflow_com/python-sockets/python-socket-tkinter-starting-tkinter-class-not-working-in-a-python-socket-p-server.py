import socket
import threading
from tkinter import *

HOST = ''
PORT = 1234

s = socket.socket()
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
receivedPos = ''

def receive(conn,addr):
    with conn, conn.makefile('r',encoding='utf8') as reader:
        while True:
            global receivedPos
            receivedPos = reader.readline()
            print(receivedPos)
            if not receivedPos:
                break
            x,y = [int(n) for n in receivedPos.split(',')]
            root.label.config(text=receivedPos)
            root.label.place(x=x, y=y)

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("1- Tkinter Changing Position")
        self.minsize(500,400)
        self.label = Label(self, text = receivedPos, bg='black', fg='blue', font='Calibri 40 bold')

root = Root()
threading.Thread(target=receive, args=(conn, addr), daemon=True).start()
root.mainloop()

