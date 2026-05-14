import json
import selectors
import socket
import types

from client.manager import Manager
from common.protocol import Message, mapping_actions


class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080
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
                receive_data = sock.recv(1024)
                if receive_data:
                    # Any data that is read is append to data.outb
                    # So it can be sent later
                    data.outb += receive_data
                    print(f"Receiving {data.outb!r}")

                else:
                    # Client has closed their socket
                    self.selector.unregister(sock)
                    sock.close()
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


import mysql.connector
import pandas as pd
from initData import initCours, initEval, initUser
from mysql.connector import Error


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
    initCours(cursor.cursor())
    initUser(cursor.cursor())
    initEval(cursor.cursor())
    cursor.commit()
    s = Server()
    s.run()
    action_a_faire = Manager.signin
    resultat = mapping_actions[Message.SIGNIN]("daniel", "daniel", "daniel")
