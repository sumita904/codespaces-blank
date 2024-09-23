"""
import requests
import re
from bs4 import BeautifulSoup

url='http://nefarious.in/'
response=requests.get(url)

if response.status_code==200:
    soup = BeautifulSoup(response.text, 'html.parser')
    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.text)
    with open('email.txt', 'w') as file:
        for e in email:
            file.write(f"{e}\n")
    print("email is successfully fetched")

else:
     print("response is not retrieved")
"""
"""
import requests
import re
from bs4 import BeautifulSoup

url='https://economictimes.indiatimes.com/markets/stocks?from=mdr'
response=requests.get(url)

if response.status_code==200:
    soup = BeautifulSoup(response.text,'html.parser')
    page_text=soup.get_text()
    updates = re.findall(r'([^.]*?market live update[^.]*\.)',page_text,re.IGNORECASE) #non greedy match
    with open('updates.txt','w') as file:
        for match in updates:
            file.write(f"{match}")
    print("updates are successfully fetched")
else:
    print("response is not retrieved")
"""

import requests
import re
from bs4 import BeautifulSoup

url= input("enter url")
search=input("enter update")
response=requests.get(url)

if response.status_code==200:
    soup = BeautifulSoup(response.text,'html.parser')
    page = soup.get_text()
    para = rf'([^.]*?{re.escape(search)}[^.]*\.)'
    report = re.findall(para,page,re.IGNORECASE)
    with open ('reports.txt','w') as file:
        for news in report:
            file.write(f"{news}\n")
    print("news is successfully fetched")
else:
    print("response is not retrieved")



