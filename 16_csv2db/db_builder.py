# Tank Engines -- Adil Gondal, Shufali Gupta
# Softdev1 pd7
# K16: No Trouble
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
c.execute("CREATE TABLE discobandit (name TEXT,age INTGEGER,id INTEGER PRIMARY KEY)") # creates discobandit table

def peep_open():
    with open("peeps.csv") as csvfile: 
        reader = csv.DictReader(csvfile)
        for row in reader: # goes row by row through csv file
            c.execute( "INSERT INTO discobandit VALUES ('" + row["name"] +"', '" +row["age"]+ "','" + row["id"] + "')") #inserts new row into discobandit table

peep_open()
#c.execute("SELECT * FROM discobandit")
#print(c.fetchall())
db.commit() #save changes
db.close()  #close database

db = sqlite3.connect("courses.db")
cur = db.cursor()
cur.execute("CREATE TABLE courses (code TEXT, mark INTEGER,id INTEGER)") # creates table for courses

def course_open():
    with open("courses.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute( "INSERT INTO courses VALUES ('" + row["code"] +"', '" +row["mark"]+ "','" + row["id"] + "')")

course_open()
db.commit()
db.close()




