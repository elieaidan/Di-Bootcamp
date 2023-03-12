import psycopg2
import random

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '12345'
DATABASE = 'test'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()

query = ""
random_number = random.randint(0,2)
if random_number == 2:
    query = "INSERT INTO table_test VALUES (DEFAULT,186,23.05,'Shon')"
else:
    query = "INSERT INTO table_test VALUES (DEFAULT,186,23.05,'Noa')"

cursor.execute(query)
connection.commit()
connection.close()






