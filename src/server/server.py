import json

import mysql.connector
import pandas as pd
from initData import initCours, initUser
from mysql.connector import Error
from xml_parser import parseUser

# from initData import


def load_json():
    with open("../DB/config.json", "r") as jsonfile:
        data = json.load(jsonfile)

    return data


def connect():
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
    cursor = connect()
    initUser(cursor.cursor())
    initCours(cursor.cursor())
    cursor.commit()
