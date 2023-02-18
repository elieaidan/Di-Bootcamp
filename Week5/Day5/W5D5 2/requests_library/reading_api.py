
import requests 
  
 
responsegoogle = requests.get('https://www.google.com')  
print(responsegoogle) 
print(responsegoogle.elapsed)


responsynet = requests.get('https://www.ynet.co.il/home/0,7340,L-8,00.html') 
print(responsynet) 
print(responsynet.elapsed)


responsimdb = requests.get('https://www.imdb.com') 
print(responsimdb) 
print(responsimdb.elapsed)


def tim_of_chargement (url):
    respons = requests.get(url)
    print(respons) 
    print(respons.elapsed)

tim_of_chargement('https://www.imdb.com')

