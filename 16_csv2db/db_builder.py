#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
c.execute("CREATE TABLE discobandit (name,age,id)")

def peep_open():
    with open("peeps.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c.execute( "INSERT INTO discobandit (name,age,id) VALUES ('" + row["name"] +"','" + row["age"] + "','" + row["id"] + "')")

peep_open()
      

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#c.execute("SELECT * FROM discobandit")
#print(c.fetchall())

#==========================================================

db.commit() #save changes
db.close()  #close database

