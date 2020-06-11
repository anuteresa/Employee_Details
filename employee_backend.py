import sqlite3

def connect():
    conn=sqlite3.connect("employees.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee (id integer primary key,firstName text,lastName text, employeeId integer, phone integer,department text)")
    conn.commit()
    conn.close()

def insert(firstName,lastName,employeeId,phone,department):
    conn=sqlite3.connect("employees.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO employee VALUES (NULL,?,?,?,?,?)",(firstName,lastName,employeeId,phone,department))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("employees.db")
    cur=conn.cursor()
    cur.execute("SELECT*FROM employee")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
#insert("Arnav","singh",134098,918273645,"IT")
#insert("Anjali","thakoor",134091,9182765675,"CS")
#insert("Reshma","Rajeev",134092,9145273645,"EC")
#insert("Amrutha","reddy",134093,918270945,"Civil")
#insert("aditya","Varma",134094,9188793645,"EEE")
#insert("Abhishek","gupta",134095,918273645,"IT")
#insert("Thejal","singh",134096,916345373645,"mech")
#insert("ayushi","kumar",134097,91874573645,"EC")
#insert("rahul","kapoor",134090,9182678645,"Civil")
#insert("vinnet","bobby",134089,918273355,"CS")
print(view())
