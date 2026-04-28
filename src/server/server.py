import json

import mysql.connector
import pandas as pd
from mysql.connector import Error

# import socket



# class Server:
#     def __init__(self, host, port):
#         host = "127.0.0.1"
#         port = 8080
#
#     def run(self):
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             s.bind((self.host, self.port))
#             s.listen()
#             conn, addr = s.accept()
#             with conn:
#                 print(f"Connected by {addr}")
#                 while True:
#                     data = conn.recv(1024)
#                     if not data:
#                         break
#                     conn.sendall(data)
#
#
def load_json():
    with open("../DB/config.json", "r") as jsonfile:
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
    connect_mySql()
