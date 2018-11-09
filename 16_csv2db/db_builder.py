# Tank Engines -- Adil Gondal, Shufali Gupta
# Softdev1 pd7
# K16: No Trouble
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops


c.execute("CREATE TABLE peeps (name TEXT,age INTGEGER,id INTEGER PRIMARY KEY)") # creates peeps table

def peep_open():
    with open("peeps.csv") as csvfile: 
        reader = csv.DictReader(csvfile)
        for row in reader: # goes row by row through csv file
            c.execute( "INSERT INTO peeps VALUES ('" + row["name"] +"', '" +row["age"]+ "','" + row["id"] + "')") #inserts new row into discobandit table

peep_open()
#c.execute("SELECT * FROM discobandit")
#print(c.fetchall())


c.execute("CREATE TABLE courses (code TEXT, mark INTEGER,id INTEGER)") # creates table for courses

def course_open():
    with open("courses.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c.execute( "INSERT INTO courses VALUES ('" + row["code"] +"', '" +row["mark"]+ "','" + row["id"] + "')")

course_open()
db.commit()
db.close()




