import requests
from bs4 import BeautifulSoup

def load_page(url):
    response = requests.get(url)
    return response.text

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    #headings = soup.find_all('h1')
    information = soup.find_all('p')
    return [information.text.strip() for information in information]


def main(url):
    html = load_page(url)
    data = extract_data(html)
    return data

if __name__ == "__main__":
    url = 'https://pypi.org/project/beautifulsoup4/'
    result = main(url)
    print(result)