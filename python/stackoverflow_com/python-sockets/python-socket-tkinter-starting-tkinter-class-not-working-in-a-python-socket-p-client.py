import socket

HOST = 'localhost'
PORT = 1234

s = socket.socket()
s.connect((HOST, PORT))

while True:
    enteredPos = input('New Position (Separate x and y with a comma, e.g.: 40,60): ')
    s.sendall(enteredPos.encode() + b'\n')
    x,y = enteredPos.split(',')
    print(f'You placed the label at {x=}, {y=}')


