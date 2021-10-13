from time import sleep
import requests
from bs4 import BeautifulSoup
import re

url= 'https://dolarhoy.com/'
page= requests.get(url) #descargo el código HTML
soup= BeautifulSoup(page.content, 'html.parser')#La compu ve la info e interpreta.Luego puedo navegar
print(page) #chequeo que funcione la conexión

blue= soup.find_all('div','tile is-child', limit=2)
print(blue)

b= blue[0] #me quedo con el 1er 'tile is-child' y saco el usd bolsa
print(b)

txt= b.get_text()
print(txt)

print(txt.find(str('b')))
print(txt.find(str('do')))

s= txt[6:40]
print(s.split())

for link in b.find_all('a'):
    print(link.get('href'))

c= b.find_all('div', class_='values')
print(c)

z= b.find_all('div',class_="compra")
print(z)

j= [i for i, e in enumerate(s) if e.isupper()]
print(j)

list= []
list= re.findall('[A-Z][^A-Z]*', s)
print(list)

texto= ' '.join(list)
print(texto)

dolar= txt.replace(txt[6:40],texto)
print(dolar)

list=dolar.split()
print(list)

print(list[1].upper())
print(list[2].upper())
