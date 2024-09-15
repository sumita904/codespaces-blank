
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

