""" #open file
path=r
with open(path,'r') as file:
    for line in file:
        print(line.strip())
"""
"""
#write over file (delete the existing data if any and replace with new one)
path=r
with open(path,'w') as file:
    file.write("Java is better\n")
    file.write("cse")
"""
"""
import os
path=r
if os.path.exists(path):
    with open(path,'r') as file:
        content=file.read()
        print(content)
else:
    print(f"file doesn't exist in {path}")
"""
"""
path=r
with open(path,'a') as file1:
     file1.write("\n Python is better than Java")
with open(path,'r') as file1:
    for line in file1:
        print(line.strip())
"""
"""
path=r
with open(path,'rb') as file:
    content=file.read() #cui 
    print(content)
#file.write(content)
"""
"""
def large_file(path):
    with open(path) as file:
        for line in file:
            yield line.strip()
for line in large_file('ExportActions (87).xlsx'):
    print(line)
"""
"""
import openpyxl
def read_excel(path):
    workbook=openpyxl.load_workbook(path)
    sheet=workbook.active
    for row in sheet.iter_rows(values_only=True):
        yield row
path=r    #large file path
for row in read_excel(path):
    print(row)

"""
"""
path=r
words=['swap','cross','ball','python']
with open(path,'r') as file:
    for line_no,line in enumerate(file,start=1):
        for word in words:
            if word in line:
                print(f"word '{word}'found on line {line_no}:{line.strip()}")
"""
"""
# web scrapping using beautifulsoup bs4
import requests
from bs4 import BeautifulSoup

url='https://www.w3schools.com/howto/howto_make_a_website.asp'
response=requests.get(url)
if response.status_code==200:
    webpage_content=response.text
    print("webpage_content fetch")
else:
    print(f"Failed to fetch webpage_content,{response.status_code}")
soup=BeautifulSoup(webpage_content, 'html.parser')
page_title=soup.title.string
print(f"page_title:{page_title}")
links=soup.find_all('a')
for link in links:
    print(link.get('href'))
  """
"""
import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/India'
response=requests.get(url)
if response.status_code==200:
    webpage_content=response.text
    print("webpage_content fetch")
else:
    print(f"failed to fetch webpage_content fetch",{response.status_code})
soup=BeautifulSoup(webpage_content,'html.parser')
paragraphs=soup.find_all('p')
links=soup.find_all('a')
for paragraph in paragraphs:
    print(paragraph.get_text())
for link in links:
    print(link.get('href'))
"""
"""
import requests
from bs4 import BeautifulSoup

url='https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_mark'
response=requests.get(url)
if response.status_code==200:
   soup=BeautifulSoup(response.text,'html.parser')
   mark_tag=soup.find('mark')
   if mark_tag:
       print(f"mark_tag is present,{mark_tag.get_text()}")
   else:
       print("mark_tag is not present")

else:
    print(f"failed to fetch webpage_content fetch",{response.status_code})
"""

# to store website data on your local computer
import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code==200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links= soup.find_all('a')
    with open('file_data.txt','w') as file:
        file.write(f"links are found :\n")
        for link in links:
            file.write(f"{link.get('href')}\n")

else:
    print(f"failed to retrieve {response.status_code}")



#user will ask to fetch from url and store that in file


















