class Book:
    """ Класс, представляющий книгу."""
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Метод возвращает строку с названием книги"""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Метод возвращает строку для создания такого же экземпляра книги"""
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
