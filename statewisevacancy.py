#!/usr/bin/env python
# coding: utf-8

# In[12]:


from bs4 import BeautifulSoup

import csv
import requests

url = "https://kpi.apiic.in:8443/KPI/apiicfi/VacantPlots.jsp?param=vacip&usrzn=ALL"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

        
filename= 'key.csv'

csv_writer=csv.writer(open(filename,'w'))

heading=soup.find('thead')
print(heading.text)

for tr in soup.find_all('tr'):
    data=[]
    
    
    for th in tr.find_all('th'):
        data.append(th.text)
        
    if(data):
        print("Inserting headers: {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue
        
    for td in tr.find_all('td'):
        data.append(td.text)
    
    if(data):
        print("Inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)
        
        
    
    


# In[ ]:




