from lib2to3.pytree import convert
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np


# NOTE: The page at the given URL is maintained by "wikipedia", which might be updated in future.

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

temp_list= []


table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance = []
solar_mass = []
solar_radius =[]

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    solar_mass.append((temp_list[i][7]))
    solar_radius.append((temp_list[i][8]))


df2 = pd.DataFrame(list(zip(Star_names,Distance,solar_mass,solar_radius,)),columns=['Star_name','Distance','Solar_Mass','Solar_Radius'])
print(df2)

df2.to_csv('solar_dwarf_stars.csv')