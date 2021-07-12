from bs4 import BeautifulSoup as bs
import pandas as pd
import requests 

URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
detail = requests.get(URL)
print(detail)

soup = bs(detail.text,"html.parser")
dwarfs = soup.find_all("table")
print(len(dwarfs))

temp=[]
rows= dwarfs[4].find_all("tr")

for tr in rows:
    td=tr.find_all("td")
    r =[i.text.rstrip() for i in td]
    temp.append(r)
print(temp)

star_name=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(temp)):
    star_name.append(temp[i][0])
    distance.append(temp[i][5])
    mass.append(temp[i][7])
    radius.append(temp[i][8])

df =pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=["star_name","distance","mass","radius"])
df.to_csv("BrownDwarf.csv")

