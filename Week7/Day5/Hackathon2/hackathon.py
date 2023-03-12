import worldometer
import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.animation import FuncAnimation
from itertools import count



current_time = datetime.now()

current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(current_time)


def open_connection():

    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = '12345'
    DATABASE = 'cause_of_death'

    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()

    return connection, cursor


def write():
    connection, cursor = open_connection()

    smoking = worldometer.deaths_caused_by_smoking_this_year()
    smoking_values = smoking['deaths_caused_by_smoking_this_year']

    alcohol = worldometer.deaths_caused_by_alcohol_this_year()
    alcohol_values =alcohol['deaths_caused_by_alcohol_this_year']


    aids = worldometer.deaths_caused_by_hiv_aids_this_year()
    aids_values= aids['deaths_caused_by_hiv/aids_this_year']

    diseases = worldometer.deaths_caused_by_water_related_diseases_this_year()
    diseases_values= diseases['deaths_caused_by_water_related_diseases_this_year']

    deaths_this_year = worldometer.deaths_this_year()
    death_values = deaths_this_year['deaths_this_year']

    cancer = worldometer.deaths_caused_by_cancer_this_year()
    cancer_values= cancer['deaths_caused_by_cancer_this_year']

    query = f"INSERT INTO cause_of_death VALUES (DEFAULT,{smoking_values},{alcohol_values},{aids_values},{diseases_values},{cancer_values},{death_values},'{current_time}')"

    cursor.execute(query)

    query = "INSERT INTO cause_of_death VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s)"
    values = (smoking_values, alcohol_values, aids_values, diseases_values, cancer_values, death_values, current_time)

    cursor.execute(query, values)
    connection.commit()

    connection.close()

def read():
    
    connection, cursor = open_connection()

    query2 = "SELECT smoking, death_in_this_year FROM cause_of_death"
    cursor.execute(query2)
    data = cursor.fetchall()
    connection.close()

    x = [row[1] for row in data]
    y = [row[0] for row in data]


    connection.close()
 

    return x,y 








def animate(i):
    try:
        x, y = read()
        print(x[i], y[i])

        plt.clf()
        plt.plot(x[:i+1], y[:i+1], label='Channel 1')

        plt.legend(loc='upper left')
        plt.tight_layout()

    except IndexError:
        print('No more data')

ani = FuncAnimation(plt.gcf(), animate, interval=10000)

plt.tight_layout()
plt.show()



