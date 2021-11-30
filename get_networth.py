#############
# Name: Ember Shan
# Using the tiktok API to get the followers and avg likes per video 
# by using the artist names in the database
#############

import json
import os
import requests
import sqlite3


def getToken():
    # get my API key from file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = dir_path + '/' + 'tokens.txt'
    f = open(path, 'r')
    t = f.readline()
    f.close()
    return t


def getNameList(cur, conn):
    # get the name list from the finalproject database
    # TODO: get only the next 25 names? 
    cur.execute("SELECT artist_id, name FROM Artists ORDER BY artist_id LIMIT 1")
    rows = cur.fetchall()
    names = []
    # craete a list of tuples with id as the first element and name as the second element 
    for r in rows: 
        names.append(tuple([r[0], r[1]]))
    return names


def getNetWorth(names):
    key = getToken()
    networth = []
    for n in names:
        # get the api request url
        api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(n[1].lower())
        print(api_url)
        try: 
            r = requests.get(api_url, headers={'X-Api-Key': key} )
            # check if the request succeeded
            if r.status_code == requests.codes.ok:
                d = json.loads(r.text)
                # create a list of tuples with name as the first and networth as the second element
                networth.append(tuple(n[1], d['net_worth']))
                
            else:
                print("Error:", r.status_code, r.text)
                return None
        except:
            print("No information about this singer found")
            return None

    return networth


def insertIntoDatabase():
    pass


def main():
    # connect to the database
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conn = sqlite3.connect(dir_path + '/' + "finalproject.db")
    cur = conn.cursor()
    # get the data and insert it into the database
    names = getNameList(cur, conn)
    print(getNetWorth(names))


if __name__ == "__main__":
    main()