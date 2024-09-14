import random
import select
import socket
import threading
import time

hostname = "example.org"
ip = "127.0.0.1"
port = 8443
client_counter = 0


def server(idle_callback):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ip, port))
    server_socket.listen(5)
    # server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # server_socket = server_context.wrap_socket(server_socket, server_side=True)

    clients = []

    while True:
        sockets = [server_socket, *clients]
        readable, writable, exceptional = select.select(sockets, [], sockets, 0.1)
        for s in readable:
            if s is server_socket:
                connection, client_address = server_socket.accept()
                connection.setblocking(False)
                clients.append(connection)
                print(f"new connection from {client_address}")
            else:  # must be a client socket
                try:
                    msg = s.recv(1024)
                    print(f"{s}: received {msg}")
                    if msg.startswith(b"The time is"):
                        s.sendall(b"The eagle flies at midnight...\n")
                    else:
                        s.sendall(f"Sorry, I don't understand {msg}\n".encode())
                except ConnectionError as exc:
                    print(f"{s}: {exc}")
                    s.close()
                    clients.remove(s)
                    continue
        for x in exceptional:
            print(f"exceptional condition on {x}")
            x.close()
            clients.remove(x)
        idle_callback()


def client():
    global client_counter
    client_counter += 1
    client_id = client_counter
    print(f"[{client_id}] Starting client...")

    with socket.create_connection((ip, port)) as client:
        # client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        # with client_context.wrap_socket(client, server_hostname=hostname) as client:
        #     print(f'Using {client.version()}\n')

        while True:
            if random.random() < 0.1:
                print(f"[{client_id}] Time to go...")
                break

            if random.random() < 0.5:
                client.sendall(f"The time is {time.asctime()}\n".encode("utf-8"))
            else:
                client.sendall(b"Hello, server\n")

            data = client.recv(1024 * 8)
            if not data:
                print(f"[{client_id}] Client received no data")
                break
            print(f"[{client_id}] Server says: {data}")
            time.sleep(0.5)


def idle_callback():
    if random.random() < 0.1:
        threading.Thread(target=client).start()


def main():
    server(idle_callback)


if __name__ == "__main__":
    main()
