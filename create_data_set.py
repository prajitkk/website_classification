# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:50:27 2018

@author: prajit kk
"""

from bs4 import BeautifulSoup
import requests

url =["https://en.wikipedia.org/wiki/Emily_Davison",
      "https://en.wikipedia.org/wiki/Polypropylene",
      "https://en.wikipedia.org/wiki/Technology",
      "https://en.wikipedia.org/wiki/Ecosystem_engineer",
      "https://en.wikipedia.org/wiki/Engineering",
      "https://en.wikipedia.org/wiki/Mechanical_engineering",
      "https://en.wikipedia.org/wiki/Robotics",
      "https://en.wikipedia.org/wiki/Brussels",
      "https://en.wikipedia.org/wiki/Metropolitan_area",
      "https://en.wikipedia.org/wiki/Brazil"]
for i in range(0,9):
    r  = requests.get(url[i])
    data = r.text
    my_data =""
    soup = BeautifulSoup(data, 'lxml')
    for link in soup.find_all('p'):
        #print(link.text)
        my_data = my_data + link.text
        my_data = my_data
    file = open("eggs.tsv","a",encoding='utf-8') 
    file.write(my_data +"\t"+"\n") 
    file.close()
    
            
