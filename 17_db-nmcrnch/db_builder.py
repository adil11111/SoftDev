#Team Old Money - Rubin P, Imad B.
#SoftDev1 pd7
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

# empty lists to store our data from the csv
data = []
individual_rows = []

#loops thru each row and adds it to the individual rows list
#then, adds that to the big data list and empties the individual rows list
with open('data/peeps.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		individual_rows.append(row['name'])
		individual_rows.append(row['age'])
		individual_rows.append(row['id'])
		data.append(individual_rows)
		individual_rows = []

#creates the table
command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGERY PRIMARY KEY)"
c.execute(command)    #run SQL statement
#executemany function goes thru a list of lists and adds each value to the table
c.executemany('INSERT INTO peeps VALUES (?, ?, ?)', data)

#repeat this process 2 more times for the other .csv files

data = []
individual_rows = []

with open('data/courses.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		individual_rows.append(row['code'])
		individual_rows.append(row['mark'])
		individual_rows.append(row['id'])
		data.append(individual_rows)
		individual_rows = []

command = "CREATE TABLE courses (name TEXT, mark INTEGER, id INTEGER)"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement
c.executemany('INSERT INTO courses VALUES (?, ?, ?)', data)

data = []
individual_rows = []

with open('data/occupations.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		individual_rows.append(row['Job Class'])
		individual_rows.append(row['Percentage'])
		data.append(individual_rows)
		individual_rows = []

command = "CREATE TABLE occupations (job TEXT, percentage NUMERIC )"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement
c.executemany('INSERT INTO occupations VALUES (?, ?)', data)

#==========================================================

db.commit() #save changes
db.close()  #close database
