from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://internshala.com/internships/work-from-home-computer-science-internships/part-time-true/")
time.sleep(1)
close = driver.find_element(By.ID, "close_popup")
close.click()

internships = []
time.sleep(1)
# container = driver.find_element(By.ID, "internship_list_container_1")
# elements = container.find_element(By.CLASS_NAME, "company")
elements = driver.find_elements(By.CLASS_NAME, "internship_meta")

# print(elements)
# elements = elements.find_elements(By.CLASS_NAME, "other_detail_item ")[2].find_element(By.CLASS_NAME, "item_body")
for el in elements:
    if len(el.find_elements(By.CLASS_NAME, "other_detail_item ")) == 3:
        title = el.find_element(By.CLASS_NAME, "company").text
        start = el.find_elements(By.CLASS_NAME, "other_detail_item ")[0].find_element(By.CLASS_NAME, "item_body").text
        duration = el.find_elements(By.CLASS_NAME, "other_detail_item ")[1].find_element(By.CLASS_NAME, "item_body").text
        stipend = el.find_elements(By.CLASS_NAME, "other_detail_item ")[2].find_element(By.CLASS_NAME, "item_body").text
        link = el.find_element(By.TAG_NAME, "a").get_attribute("href")
        data = [title, start, duration, stipend, link]

        internships.append(data)

for x in internships:
    print(f'INTERNSHIP NAME: {x[0]}')
    print(f'INTERNSHIP START DATE: {x[1]}')
    print(f'INTERSHIP DURATION: {x[2]}')
    print(f'SCHOLARSHIP LINK: {x[3]}')
    print("------------------------------------------------------------")
print(len(internships))