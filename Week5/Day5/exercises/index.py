import requests
import time

url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(url)



# while True:
#     response = requests.get(url) # get connect to url

#     # Response [200] -> success
#     # Response [400] -> failure 

#     print(response) 

#     data = response.json()

#     print(data['value'])

#     time.sleep(1) # make program sleep 1 seconds
