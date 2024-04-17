import os
import json

# Определение класса BookmarkManager
class BookmarkManager:
    def __init__(self, directory):
        self.directory = directory
        self.file_path = os.path.join(directory, 'bookmarks.json')
        self.load_bookmarks()


# Функция для загрузки закладок из файла
    def load_bookmarks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.bookmarks = json.load(file)
        else:
            self.bookmarks = {}

    # Функция для сохранения закладок в файл
    def save_bookmarks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.bookmarks, file)

    # Функция для добавления закладки
    def add_bookmark(self, url, title):
        self.bookmarks[url] = title
        self.save_bookmarks()

    # Функция для удаления закладки
    def remove_bookmark(self, url):
        if url in self.bookmarks:
            del self.bookmarks[url]
            self.save_bookmarks()
        else:
            print("Закладка не найдена.")

    # Функция для вывода списка всех закладок
    def list_bookmarks(self):
        if self.bookmarks:
            print("Закладки:")
            for url, title in self.bookmarks.items():
                print(f"{title}: {url}")
        else:
            print("Закладки не сохранены.")

    # Функция для открытия закладки в браузере
    def open_bookmark(self, url):
        if url in self.bookmarks:
            print(f"Открывается закладка: "
                  f"{self.bookmarks[url]} - {url}")
        else:
            print("Закладка не найдена.")

# Основная функция
def main():
    directory = input("Введите каталог для сохранения закладок: ")
    if not os.path.exists(directory):
        os.makedirs(directory)

    bookmark_manager = (BookmarkManager(directory))

    while True:
        print("\nМеню:")
        print("1. Добавить закладку")
        print("2. Удалить закладку")
        print("3. Список закладок")
        print("4. Открыть закладку")
        print("5. Выйти")

        choice = input("Введите ваш выбор: ")
        if choice == "1":
            url = input("Введите URL: ")
            title = input("Введите название: ")
            bookmark_manager.add_bookmark(url, title)
        elif choice == "2":
            url = input("Введите URL для удаления: ")
            bookmark_manager.remove_bookmark(url)
        elif choice == "3":
            bookmark_manager.list_bookmarks()
        elif choice == "4":
            url = input("Введите URL для открытия: ")
            bookmark_manager.open_bookmark(url)
        elif choice == "5":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()