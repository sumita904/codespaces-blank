#user will ask to fetch from url and store that in file
"""
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
"""

import requests
from bs4 import BeautifulSoup

url='https://timesofindia.indiatimes.com/city/mumbai'
response=requests.get(url)

if response.status_code==200:
    soup= BeautifulSoup(response.content,'html.parser')
    page=soup.get_text()
    path=r'C:\Users\v-sumikumari\PycharmProjects\LearnPy7DaysDemo\pythonProject\Day6_Operator\full_data.txt'
    try:
        with open(path,'w',encoding='utf-8') as file:
            file.write(page)
        print("data successfully returned")
    except Exception as e:
        print(f"error={e}")
else:
    print("failed to get data")


"""
#it sets the word boundary
r # raw string
[a-z]   # (it can be anything in between a to z)
[0-9]   # (it can be anything in between 0 to 9)
[._%+-]  #these other special characters can be taken(if other special character needed then to be added inside the braces
[]+      #one or more chara of it's preceeding characters can be taken
# \.
{4,}    #minimum 4 letters required
[A-Z|a-z] 
"""
