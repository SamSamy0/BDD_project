import json

import mysql.connector
import pandas as pd
from initData import initCours, initEval, initUser
from mysql.connector import Error


def load_json():
    with open("../DB/config.json", "r", encoding="utf-8") as jsonfile:
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
    initCours(cursor.cursor())
    initUser(cursor.cursor())
    initEval(cursor.cursor())
    cursor.commit()
