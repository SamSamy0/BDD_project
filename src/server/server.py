import json
import selectors
import socket
import types

import mysql.connector
from ServerNetworkManager import ServerNetworkManager



class Server:
    def __init__(self, cursor):
        self.host = "127.0.0.1"
        self.port = 8080
        self.manager = ServerNetworkManager(cursor)
        self.selector = selectors.DefaultSelector()

    def accept(self, sock):
        conn, addr = sock.accept()
        print(f"Connected to {addr}")
        conn.setblocking(False)
        # Fetching data from client
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        # Because we want to know when the client reads and writes
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.selector.register(conn, events, data=data)

    def serve_connection(self, key, mask):
        # Key is the socket object
        sock = key.fileobj
        data = key.data

        # Mask contains the events that are ready (0 if not ready, 1 else)
        if mask & selectors.EVENT_READ:
            try:
                receive_data = sock.recv(65536)
                if receive_data:
                    # Any data that is read is append to data.outb
                    # So it can be sent later
                    request_str = receive_data.decode("utf-8")
                    request_dict = json.loads(request_str)
                    print(f"Requete recu : {request_dict}")

                    reponse_dict = self.manager.handle_request(request_dict)

                    data.outb += json.dumps(reponse_dict,default=str).encode("utf-8")
                else:
                    # Client has closed their socket
                    self.selector.unregister(sock)
                    sock.close()
            except json.JSONDecodeError:
                print("Erreur : Le message reçu n'est pas un JSON valide.")
            except ConnectionResetError:
                # Handles the case where the client closes the connection suddenly
                self.selector.unregister(sock)
                sock.close()

        if mask & selectors.EVENT_WRITE:
            # When ready to send data to clients, echo data.outb
            if data.outb:
                print(f"Sending {data.outb!r}")
                # .send returns nb of bytes sent
                sent = sock.send(data.outb)

                # nb of bytes sent is used as slice to delete what's sent
                data.outb = data.outb[sent:]

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lsock:
            lsock.bind((self.host, self.port))
            lsock.listen()
            # Socket not in blocking mode
            lsock.setblocking(False)

            # Every new socket is saved in selector
            self.selector.register(lsock, selectors.EVENT_READ, data=None)
            try:
                # Event loop
                while True:

                    # Blocked until socket ready for I/O
                    events = self.selector.select(timeout=None)
                    for key, mask in events:
                        if key.data is None:
                            self.accept(key.fileobj)
                        else:
                            self.serve_connection(key, mask)
            except KeyboardInterrupt:
                print("Server ended")

            finally:
                self.selector.close()


def load_json():
    with open("DB/config.json", "r") as jsonfile:
        data = json.load(jsonfile)

    return data


def connect_mySql():
    connection = None
    init = load_json()
    connection = mysql.connector.connect(
        host=init["host"],
        port=init["port"],
        user=init["user"],
        password=init["password"],
        database=init["database"],
    )
    print("MySQL Database connection successful")
    return connection


if __name__ == "__main__":
    cursor = connect_mySql()
    cursor.commit()
    s = Server(cursor)
    s.run()
