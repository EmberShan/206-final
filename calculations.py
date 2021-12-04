import json
import os
import requests
import sqlite3

def getData(cur):
    
    pass


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conn = sqlite3.connect(dir_path + '/' + "finalproject.db")
    cur = conn.cursor()
    getData(cur)


if __name__ == "__main__":
    main()