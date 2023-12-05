# Author: Emsii 
# Date: 5.12.2023
# https://github.com/EmsiiDiss

#InProgrogress!!!


import DataBaseConnect
import traceback
import os.path

def first_test_connect():
    if os.path.isfile("C:\GitHUB\Base.db") == True:
        connect = DataBaseConnect.connect("C:/GitHUB/")
    else:
        path = input("Show the DB way! \n  Enter 0 to create DB! \n")
        if path == "0":
            connect = DataBaseConnect.connect("")
        else:    
            connect = DataBaseConnect.connect(path)  
    print("Connected!")
    return connect

def main(connect):
    DataBaseConnect.table_maker(connect)

if __name__ == '__main__':
    try:
        path = first_test_connect()
        main(path)
    except:
        traceback.print_exc()             