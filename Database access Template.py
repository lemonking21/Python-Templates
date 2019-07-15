################################################################################
# Created By Kyle Krug
# Created on 7/9/2019
# Created to form a tempate on how to access a sql database and how to extract 
# data from the database
################################################################################

import pyodbc
#make us of pyodbc to access database


server_name = "" #This can be found on the connect to server login, it will be listed as the Server Name
db_name = "" # This can be found in the database folder once you have logged in
#these will be used below to ACCESS the correct database 

tripcon = pyodbc.connect('driver = {sql server}';
                      'server=server_name;'
                      'database=db_name;'
                      'trusted_Connection=yes;')
# you can get the sql server, sever name and the db_name( database name from accessing the database)


cursor = tripcon.cursor()
#this is used to connect to the database


cursor.execute('SELECT * FROM db_name.Table')
# this will select all records in the databse 



for row in cursor:
    print(row)
    #this is used to print the database table

