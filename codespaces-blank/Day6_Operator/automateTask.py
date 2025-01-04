"""
import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import schedule
from selenium.webdriver.common.by import By

driver_path=r"/Users/sumitasinha/Downloads/chromedriver-mac-arm64/chromedriver"
options=Options()
options.add_argument("user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

service=Service(driver_path)
driver=webdriver.Chrome(service=service,options=options)
output_file="new.arrival.txt"
output_file_path=os.path.abspath(output_file)
try:
    driver.get("https://www.flipkart.com/")
    try:
        close_button=driver.find_element(By.XPATH,"//button[contains(text(),'X')]")
        close_button.click()
    except Exception as e:
        print("no logging popup to close")
    time.sleep(3)
    search_box=driver.find_element(By.NAME,"q")
    search_box.send_keys("new arrivals 5g mobile")
    search_box.submit()
    time.sleep(10)
    mobiles=driver.find_elements(By.XPATH,"//div[contains(@class,'CGtC98')]//a[contains(@href,'/Mobile/')]/ancestor::div[contains(@class,'CGtC98')]")
    if not mobiles:
        print("no new arrivals of mobiles found")
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
"""

import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")


service = Service("/Users/sumitasinha/Downloads/chromedriver_mac_arm64 (1)/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)


url = "https://www.flipkart.com/search?q=new+arrivals+mobiles"


def job():
    driver.get(url)
    time.sleep(5)


    mobiles = driver.find_elements(By.CLASS_NAME, "KzDlHZ")
    prices = driver.find_elements(By.CLASS_NAME, "Nx9bqj _4b5DiR")


    results = []
    for mobile, price in zip(mobiles, prices):
        results.append(f"{mobile.text} - {price.text}")

    with open("new_arrivals_mobiles.txt", "w") as file:
        file.write("\n".join(results))

    print(f"Scraped {len(results)} mobiles. Data saved to 'new_arrivals_mobiles.txt'.")

schedule.every(1).minutes.do(job)

print("Task scheduled. Press Ctrl+C to stop.")


while True:
    schedule.run_pending()
    time.sleep(1)