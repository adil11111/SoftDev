#Hmmmm - Imad Belkebir, Adil Gondal
#SoftDev1 pd7
#K17 -- Average
#2018-10-05

import sqlite3   #enable control of an sqlite database

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
db.text_factory = str         #change data from fetchall() from unicode to utf

#=======================================================================

command = "CREATE TABLE peeps_avg (name TEXT, id INTEGER, average INTEGER)"
c.execute(command)

data = []

command = "SELECT peeps.name, peeps.id FROM peeps" #retrieves name and id of all peeps
c.execute(command)

for peep in c.fetchall(): #cycles through retrieved peeps
    individual_data = []
    command = "SELECT courses.mark FROM courses WHERE courses.id = " + str(peep[1]) #get marks with corresponding id of current peep
    c.execute(command)
    sum = 0
    num = 0
    for mark in c.fetchall(): #cycle through retrieved marks to calculate average
        sum += mark[0]
        num += 1
    sum /= num
    individual_data.append(peep[0])
    individual_data.append(peep[1])
    individual_data.append(sum)     #create row for current peep
    data.append(individual_data)    #insert row into data

c.executemany("INSERT INTO peeps_avg VALUES (?, ?, ?)", data) #insert all individual into table peeps_avg

def insertRow(code, mark, id):
    row = [code, mark, id]
    c.execute("INSERT INTO courses VALUES (?, ?, ?)", row)

db.commit()
db.close()
