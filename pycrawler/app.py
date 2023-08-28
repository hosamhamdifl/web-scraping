import requests
from bs4 import BeautifulSoup
import csv

response=requests.get('https://stackoverflow.com/questions')
soup=BeautifulSoup(response.text,'html.parser')
questions = soup.select('.s-post-summary.js-post-summary')

print(questions[10].get("id",0))
print(questions[10].select_one('.s-link').get_text())

with open('questions.csv','w',encoding='utf-8') as f:
    w=csv.writer(f)
    w.writerow(['id','link'])
    for q in questions:
        print(q.get("id",0))
        print(q.select_one('.s-link').get_text())
        w.writerow([q.get("id",0),q.select_one('.s-link').get_text()])
    
    

# print(soup)
# print(soup.find_all)