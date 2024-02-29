
import mysql.connector
#from dotenv import load_dotenv
#import os

# Load environment variables
#load_dotenv()

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Goofy77871998$"
MYSQL_DB = "example"

# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )


def show_tables():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    x = cursor.fetchall()

    li = []

    for rows in x:
        li.append(rows[0])

    print(li)
    conn.close()

    return li

def show_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PEOPLE")
    x = cursor.fetchall()

    li = []

    for rows in x:
        lis = []
        lis.append(rows[0])
        lis.append(rows[1])
        lis.append(rows[2])
        li.append(lis)

    print(li)
    conn.close()

    return li

def initialize_db():
    conn = connect()
    cursor = conn.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS people (
        people_id SMALLINT AUTO_INCREMENT,
        fname VARCHAR(255),
        lname VARCHAR(255),
        CONSTRAINT pk_people_id PRIMARY KEY (people_id)
    )
    '''
    cursor.execute(query)
    conn.close()

def add_person(firstName:str , lastName:str ):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO people (fname, lname) VALUES (%s,%s)"
    values = (firstName, lastName)
    cursor.execute(query, values)
    conn.commit()
    conn.close()

    return cursor.lastrowid
