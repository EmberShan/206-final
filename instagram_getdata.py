import json
import os
import sqlite3
import bs4
import requests

dir_path = os.path.dirname(os.path.realpath(__file__)) 


def getURL(name):
    base = 'https://www.instagram.com/web/search/topsearch/?context=blended&query='
    url = base + name.lower()

    

def getDataFromIns():
    # TODO: using requests to retrieve the data

    # store the data in a json file
    pass


def createDatabase():
    # get data from json file and use it to create the db
    pass


def main():
    # get the access token for Instagram graph API
    getToken()

    


if __name__ == "__main__":
    main()