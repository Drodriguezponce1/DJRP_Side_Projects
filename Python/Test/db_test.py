import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Goofy77871998$",
  database= "example"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW Tables")

x = mycursor.fetchall()

li = []
for rows in x:
  li.append(rows[0])

print(li)

def fun(lname :int, fnam :str):
  return lname + fnam

print(fun("f",2))