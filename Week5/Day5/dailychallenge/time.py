import requests
import time

url= 'https://www.google.com/?client=safari'

response = requests.get(url)

open_time = time()

output = url.read()



close_time = time()

print(f'The loading time of website is',round(close_time-open_time,3))