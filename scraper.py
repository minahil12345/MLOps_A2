import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


# URLs of the websites
urls = {
    'dawn': 'https://www.dawn.com',
    'bbc': 'https://www.bbc.com/news'
}

def dawnExtract():
    # Fetch the webpage
    response = requests.get(urls['dawn'])
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract links
    links = [link.get('href') for link in soup.find_all('a', {'class': 'story__link'}, href=True)]

    # Display the extracted data
    print("Links from Dawn:")
    for link in links:
        # validate the link
        if not link.startswith('https://www.dawn.com'):
            continue

        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.select('div.template__header.flow-root.px-1.border-b.mb-4 > h2 > a')
        descriptions = [desc.get_text() for desc in soup.find_all('p')]

        # append description to one paragraph
        description = ''
        for desc in descriptions:
            description += desc + ' '
        
        # write the title and description to a file 
        with open('./data/dawn.txt', 'a') as f:
            if len(titles) > 0:
                f.write('Title : '+ titles[0].get_text() + '\n')
                f.write('Description : ' +description + '\n\n')

def bbcExtract():
    url = urls['bbc']

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
            f.write('Description : ' + description[i].text + '\n\n')

driver.quit()

dawnExtract()
bbcExtract()