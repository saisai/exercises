import socket
import os

BLOCK = 128 << 10 # 128KB

with socket.socket() as server:
    server.bind(('', 9999))
    server.listen()

    while True:
        client, addr = server.accept()
        try:
            with (client,
                  client.makefile('rb') as rfile,
                  client.makefile('wb') as wfile):

                while True:
                    filename = rfile.readline()
                    if not filename: break

                    fullname = os.path.join('Server_files', filename.decode().rstrip('\n'))
                    file_size = os.path.getsize(fullname)
                    wfile.write(f'{file_size}\n'.encode())
                    print(f'Sending {fullname}...')
                    with open(fullname, 'rb') as file:
                        while data := file.read(BLOCK):
                            wfile.write(data)
                    wfile.flush() # make sure anything remaining in makefile buffer is sent.
                    print(f' Complete ({file_size} bytes).')
        except ConnectionResetError:
            print('Client aborted.')
