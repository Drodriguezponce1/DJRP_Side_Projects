import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Goofy1998$",
  database= "sakila"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW Tables")

x = mycursor.fetchall()

li = []
for rows in x:
  li.append(rows[0])

print(li)

def fun(lname :str, fnam :str):
  return lname + fnam

print(fun("f","sdf"))