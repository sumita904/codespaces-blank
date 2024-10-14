"""

import re

import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/India"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
response=requests.get(url,headers=headers)

if response.status_code==200:
    soup=BeautifulSoup(response.text,'html.parser')
    page=soup.get_text()
    deal=re.findall(r'india',page)
    with open('file_data1.txt','w') as file:
        file.write(f"best deals are found:\n")
        for deals in deal:
            file.write(f"{deals.get_text()}")

else:
    print(f"response is not retrieved {response.status_code}")

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

from selenium.webdriver.common.by import By

driver_path=r"/Users/sumitasinha/Downloads/chromedriver-mac-arm64/chromedriver"
options=Options()
options.add_argument("user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")

service=Service(driver_path)
driver=webdriver.Chrome(service=service,options=options)
output_file="mobiles.txt"
output_file_path=os.path.abspath(output_file)
try:
    driver.get("https://www.flipkart.com/")
    try:
        close_button=driver.find_element(By.XPATH, "//button[contains(text(),'X')]")
        close_button.click()
    except Exception as e:
        print("no logging popup to close")
    time.sleep(3)
    search_box=driver.find_element(By.NAME,"q")
    search_box.send_keys("mobile")
    search_box.submit()
    time.sleep(10)
    mobiles=driver.find_elements(By.XPATH,"//div[contains(@class,'tUxRFH')]//a[contains(@href,'/mobile/')]/ancestor::div[contains(@class, 'tUxRFH')]")
    if not mobiles:
        print("no mobiles found")
    with open(output_file,'w',encoding='utf-8') as file:
        for mobile in mobiles:
            try:
                name=mobile.find_element(By.XPATH, ".//div[contains(@class, 'C7fEHH')]").text
                price=mobile.find_element(By.XPATH, ".//div[contains(@class, 'Nx9bqj CxhGGd')]").text
                print(f"mobile_name{name},price{price}")
                file.write(f"mobile_name{name},price{price}")
            except Exception as e:
                print("couldn't extract mobile details")
    print(f"data has been stored{output_file_path}")
except Exception as e:
    print("error occurred")

finally:
    driver.quit()




