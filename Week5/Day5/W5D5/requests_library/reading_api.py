import requests
import time

url = 'http://api.open-notify.org/iss-now.json'

while True:
    response = requests.get(url) # get connect to url

    # Response [200] -> success
    # Response [400] -> failure 

    print(response) 

    data = response.json()

    print(data['iss_position'])

    time.sleep(1) # make program sleep 1 seconds