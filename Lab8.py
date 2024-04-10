import requests
from bs4 import BeautifulSoup

# Функция для загрузки HTML-страницы
def load_page(url):
    response = requests.get(url)
    return response.text

# Функция для извлечения данных из HTML-страницы
def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Например, найдем все заголовки на странице
    headings = soup.find_all('h1')
    return [heading.text.strip() for heading in headings]

# Основная функция, объединяющая все шаги скрапинга
def main(url):
    html = load_page(url)
    data = extract_data(html)
    return data

# Пример использования
if __name__ == "__main__":
    url = 'https://vilniustech.lt/index.php?lang=2'
    result = main(url)
    print(result)
