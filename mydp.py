import mysql.connector

dataBase= mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='root')

#prepare cursor object
cursorObject=dataBase.cursor()

#CREATE THE DATABASE
cursorObject.execute("CREATE DATABASE olderco")