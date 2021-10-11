import os
import platform

LOCATION =r"instantclient-basic-windows.x64-11.2.0.4.0\instantclient_11_2"

print("ARCH:", platform.architecture())
print("FILES AT LOCATION:")
for name in os.listdir(LOCATION):
    print(name)

os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

import cx_Oracle
print(cx_Oracle.version)  
cx_Oracle.clientversion()  


connection = cx_Oracle.connect(
    user="demo",
    password="demo",
    dsn="localhost/orcl3")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

def test(cursor):
    for row in cursor.execute('select * from tablenames'):
        print(row)
            
#test(cursor)
    
# https://github.com/oracle/python-cx_Oracle/issues/319