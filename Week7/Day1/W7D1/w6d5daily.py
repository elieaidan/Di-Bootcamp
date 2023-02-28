import requests 
import psycopg2
import random

url = 'https://restcountries.com/v3.1/all'

response = requests.get(url)

print(response) # if 200 - SUCCESS. IF 400, 404 - FAILURE

data = response.json() # list 


for _ in range(10):

    country = random.choice(data) # choice takes randomly an item from a list

    name = country['name']['common']
    capital = country['capital'][0]
    flag = country['flag']
    subregion = country['subregion']
    population = country['population']

    USERNAME = 'yussiroz'
    DATABASE = 'dailyW6'
    HOSTNAME = 'localhost'
    PASSWORD = 'cluster'

    connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname= DATABASE)

    cursor = connection.cursor()

    query = f"insert into countries(name, capital, flag, subregion, population) values ('{name}', '{capital}', '{flag}', '{subregion}', {population})"

    cursor.execute(query)

    connection.commit()

connection.close()