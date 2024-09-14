#user will ask to fetch from url and store that in file

import requests
from bs4 import BeautifulSoup

url= str(input("enter url"))
response=requests.get(url)

if response.status_code==200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links= soup.find_all('a')
    paras= soup.find_all('body')
    with open('file_data.txt', 'w') as file:
        file.write(f"links are found :\n")
        for link in links:
            file.write(f"{link.get('href')}\n")
        file.write(f"paragraphs are found:\n")
        for para in paras:
            file.write(f"{para.get_text()}\n")

    print("Data successfully written to 'file_data.txt'")
else:
    print(f"failed to retrieve {response.status_code}")