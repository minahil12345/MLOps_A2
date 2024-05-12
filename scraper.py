import requests
from bs4 import BeautifulSoup

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
    # Fetch the webpage
    response = requests.get(urls['bbc'])
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract links
    links = [link.get('href') for link in soup.find_all('a', href=True)]

    # Display the extracted data
    print("Links from BBC:")
    for link in links:
        # validate the link
        if not link.startswith('/news/articles'):
            continue

        new_link = 'https://www.bbc.com' + link

        response = requests.get(new_link)
        print(new_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
        titles = [desc.get_text() for desc in soup.find_all('h1')]
        descriptions = [desc.get_text() for desc in soup.find_all('p')]

        # append description to one paragraph
        description = ''
        for desc in descriptions:
            description += desc + ' '

        for title in titles:
            print(title.get_text())

        # print('Title : ',titles[0].get_text())
        print('Description : ',description)
        
        # write the title and description to a file
        # with open('./data/bbc.txt', 'a') as f:
        #     if len(titles) > 0:
        #         f.write('Title : ', titles[0].get_text() + '\n')
        #         f.write('Description : ',description + '\n\n')

dawnExtract()
bbcExtract()