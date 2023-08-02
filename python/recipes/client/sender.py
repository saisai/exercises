"""
client that sends the file (uploads)
"""

import socket
import os
import argparse

import tqdm

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 1024 * 4

def send_file(filename, host, port):
    # get the file size
    print(filename)
    print(host)
    print(port)
    filesize = os.path.getsize(filename)

    # create the client socket
    s = socket.socket()
    print(f"[+] connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] connected.")

    # send the filename and file size
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

    with open(filename, "rb") as  f:
        for _ in progress:
            #read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use send all to assure transimmiosn in
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))


    # close the socket
    s.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simple file Sender")
    parser.add_argument("file", help="File name to send")
    parser.add_argument("host", help="The host/IP address of the receiver")
    parser.add_argument("-p", "--port", help="Port to use, default is 5001", default=5001)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port
    print('host', host)
    print("port", port)
    send_file(filename, host, int(port))

    # python sender.py sender.py 192.168.0.150 --port=20000
