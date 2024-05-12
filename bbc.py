from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.bbc.com/news'

driver.get(url)

# Wait for the page to fully render
driver.implicitly_wait(10)

# Extract the headlines
headlines = driver.find_elements(By.CSS_SELECTOR, '.sc-4fedabc7-3.zTZri')
description = driver.find_elements(By.CSS_SELECTOR, '.sc-b8778340-4.kYtujW')

# write the title and description to a file
with open('./data/bbc.txt', 'a') as f:
    for i in range(len(headlines)):
        f.write('Title : ' + headlines[i].text + '\n')
        if i < len(description):
            f.write('Description : ' + description[i].text + '\n\n')




driver.quit()