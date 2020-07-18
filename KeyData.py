#!/usr/bin/env python
# coding: utf-8

# In[50]:


from bs4 import BeautifulSoup
import requests
import csv


url = "https://kpi.apiic.in:8443/KPI/apiicfi/VacantPlots.jsp?param=vacz"
html_content = requests.get(url).text


soup = BeautifulSoup(html_content, "lxml")

rows = table.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        table = soup.find('table',{'width':"48%"})

with open("editors.csv", "wt+", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        csv_row = []
        for cell in row.findAll(["tr", "td"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)
        


# In[ ]:




