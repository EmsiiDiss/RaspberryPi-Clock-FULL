# Author: Emsii 
# Date: 5.12.2023
# https://github.com/EmsiiDiss

import sqlite3
import datetime

def connect(path):
    connect = sqlite3.connect(path + 'Base.db')
    return connect


def table_maker(connect):
    
    cur = connect.cursor()

    listOfTables = cur.execute(
        """SELECT name FROM sqlite_master WHERE type='table' 
        AND name='Date'; """).fetchall()

    if listOfTables == []:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Date (
            id INTEGER PRIMARY KEY ASC,
            name varchar(250) NOT NULL,
            value varchar(250) NOT NULL
            )""") 
        
        list = [
             (1, 'api_key', str(input("ENTER api_key \n"))),
             (2, 'base_url', str(input("ENTER base_url \n"))), 
             (3, 'localization-url', str(input("ENTER localization-url \n"))),
             (99, 'time-update', str(datetime.datetime.now()))
             ]
        cur.executemany('INSERT INTO Date VALUES(?, ? , ?)', list)
    
    else:
        print(datetime.datetime.now())
        cur.execute('UPDATE Date SET value=? WHERE id=?;', (datetime.datetime.now(), 99))   
        print('Table found!')

    connect.commit()
    connect.close()		
