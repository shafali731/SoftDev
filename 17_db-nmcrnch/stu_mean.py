#Clara Mohri
#SoftDev1 pd08
#K17 -- Average
#2018-10-07

import sqlite3 #enable control of an sqlite database

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

#to look up each student's grades: (using id)
def lookup_id(id):
    command = "SELECT mark, code from courses where id = "
    command += str(id)
    c.execute(command)
    retList = []
    for i in c.fetchall():
        retList.append(i[0])
    return retList
'''
print(lookup_id(3))
print(lookup_id(1))
print(lookup_id(100))
'''
#compute each student's average, given id 
def compute_avg(id):
    grades = lookup_id(id)
    sum = 0
    for i in grades:
        sum += i
    try:
        avg = sum / len(grades)
    except:
        avg = 0
    return avg
'''
print(compute_avg(3))
print(compute_avg(1))
print(compute_avg(100))
'''
#Create a table of IDs and associated averages, named "peeps_avg"
def create_table():
    command = "CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)"
    c.execute(command)
    command = "SELECT id from peeps"
    c.execute(command)
    for i in c.fetchall():
        ide = str(i[0])
        avg = str(compute_avg(ide))
        command = "INSERT INTO peeps_avg VALUES({0}, {1})".format(ide, avg)
        c.execute(command)
    
create_table()

#display each student's name, id, and average
def display(id):
    retList = []
    command = "SELECT name from peeps where id =\"{}\"".format(str(id))
    c.execute(command)
    for i in c.fetchall():
        name = i[0]
        retList.append(name)
    command = "SELECT id, avg from peeps_avg where id = {0}".format(str(id))
    c.execute(command)
    for i in c.fetchall():
        retList.append(i[0])
        retList.append(i[1])
    return retList
'''
print(display(1))
print(display(3))
print(display(100))
'''

#Facilitate adding rows to the courses table
def add_courses(code, mark, id):
    strcode = "'" + code + "'"
    command = "INSERT INTO courses VALUES({0}, {1}, {2})".format(strcode, str(mark), str(id))
    c.execute(command)

'''
add_courses("art", 92, 11)
add_courses("systemz", 99, 11)
'''

db.commit() #save changes
db.close() #close database

