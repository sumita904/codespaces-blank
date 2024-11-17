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
output_file="profile.txt"
output_file_path=os.path.abspath(output_file)
try:
    driver.get("https://www.linkedin.com/in/sumita-kumari-01575757/")
    try:
        close_button=driver.find_element(By.XPATH,"//button[contains(text(),'X')]")
        close_button.click()
    except Exception as e:
        print("no logging popup to close")
    time.sleep(3)
    search_box=driver.find_element(By.NAME,"q")
    search_box.send_keys("sumita")
    search_box.submit()
    time.sleep(10)
    search=driver.find_elements(By.XPATH,"//input(@type='search')")
    if not search:
        print("no profiles found")
    with open(output_file,'w',encoding='utf-8') as file:
        for sumita in search:
            try:
                name=sumita.find_element(By.XPATH,".//input(@type='search')").text
                print(f"profile_name{name}")
                file.write(f"profile_name{name}")
            except Exception as e:
                print("no name with sumita is found")
        print(f"data has been stored{output_file_path}")
except Exception as e:
    print("error occurred")

finally:
    driver.quit()



    
