# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:01:42 2021

@author: Melina
"""
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://www.tripadvisor.co.uk/Restaurants-g186216-United_Kingdom.html'
html = requests.get(url)
html.status_code

soup = BeautifulSoup(html.content,'lxml')
cities = []
links = []

geo_names = soup.findAll('div',{'class':'geo_name'})
for c in geo_names:
    names = c.text
    names = names.strip('\n')
    names = names.strip('Restaurants')
    names = names.strip(' ')
    cities.append(names)
    ref = c.find('a').attrs['href']
    links.append('https://www.tripadvisor.co.uk'+ref)

#print(cities)
#print(links)
#print('------------------')

for i in range (20) :
    city = cities[i]
    link = links[i]
    html = requests.get(link)
    soup1 = BeautifulSoup(html.content, 'lxml')
    cont = soup1.findAll('div',{'class':'_3X_xCrG'})
    spans = soup1.find('span',{'class':'_1D_QUaKi'})
    
    #spans = soup1.find('span', {'class':'_1D_QUaKi'})
    #spans = soup1.findAll('span', "_1D_QUaKi")
    #spans = soup1.findAll('span', attr = {'class' : '_1D_QUaKi'})
    #spans = soup1.find('span').attr['class' : '_1D_QUaKi']
    #for span in spans:
    #vegan = spans.text.strip() 
    #print(spans)

vegan_friendly_restaurants = [4232,430,437,649,507,440,386,378,
                              310,228,233,250,263,391,218,217,
                              144,80,177,179]


plt.figure()
plt.rcdefaults()
plt.barh(cities,vegan_friendly_restaurants)
plt.xlabel('Vegan option restaurants per capita')
plt.ylabel('Top 20 Cities in UK')
plt.show()

