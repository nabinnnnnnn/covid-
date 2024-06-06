from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests
import plotly.express as px
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
soup = BeautifulSoup(soup.text, "lxml")
print(soup.contents)

table_codes = soup.table
tags = table_codes.find_all('tr')
list_data = []
for i in tags:
    list_data.append(i.text.split('\n')[1:])
cleaned_data = []
for j in list_data:
    if j[0]!= '':
          cleaned_data.append(j)
print(cleaned_data)
with open('covid_data.csv', 'w') as file:
     x = csv.writer(file)
     x.writerows(cleaned_data)


df = pd.read_csv('covid_data.csv', encoding= 'latin')
df1 = df[['Country,Other', 'TotalCases','TotalDeaths']].iloc[0:100]     
df1['TotalCases'] = [int(i.replace(',', '')) for i in df1['TotalCases']]
df1['TotalDeaths'] = [int(i.replace(',', '')) for i in df1['TotalDeaths']]
fig = px.pie(df1,names='Country,Other', values= = 'TotalDeaths', title="fhfhh gfdg ")
fig.show()

     




