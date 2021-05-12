# reboot-assessment

I use Anaconda Spyder Python version 3.8.
I managed to extract and save the names of the top 20 cities of UK and the corresponding URL for restaurants.
I turn URLs into HTMLs by using a library package requests. And then by BeautifulSoup package I extract the contents of the desired HTMLs such as the names ,restaurants etc. 
Applying the filter of vegan friendly options the URL was not different so I could not follow the same process.
Trying to inspect where to find the data for vegan friendly restaurants, I found the class '_1D_QUaKi ' of span that inludes the number of vegan friendly restaurants per capita but I did not make it to extract it automatically like the above data.
In comments some attemps can be seen.
In order to complete the task of visualizing the data I created a list and saved manually the number of vegan friendly restaurants per capita according to the list of names.
I understand that this is not an accepted way to extract data however I really wanted to complete the task anyhow.


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


