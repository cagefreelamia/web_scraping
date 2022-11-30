from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
scholarships = []
driver.get("https://www.wemakescholars.com/scholarship/search?nationality=64&interest=42-43-44-45-46-47-48-1-2-3-4-5-6-7-8-9-40-41-49-35-36-54&country=64&study=2")
time.sleep(1)
elements = driver.find_elements(By.CLASS_NAME,"post")
for el in elements:
    title = el.find_element(By.CLASS_NAME,"post-title")
    last_date = el.find_element(By.TAG_NAME, "span")
    eligible = el.find_element(By.CLASS_NAME, "col-md-6").find_element(By.TAG_NAME, "span")
    image_link = el.find_element(By.TAG_NAME, "img")
    reg_link = el.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
    temp = [title.text, last_date.text, eligible.text, image_link.get_attribute("src"), reg_link.get_attribute("href")]
    scholarships.append(temp)

# print(len(scholarships))
for x in scholarships:
    print(f'SCHOLARSHIP NAME: {x[0]}')
    print(f'SCLARSHIP LAST DATE: {x[1]}')
    print(f'SCHOLARSHIP APPLICABLE FOR: {x[2]}')
    print(f'SCHOLARSHIP LINK: {x[4]}')
    print("------------------------------------------------------------")

driver.quit()