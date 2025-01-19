class Library:
    """ Класс для библиотеки книг"""
    def __init__(self, books=None):
        """Инициализация библиотеки со списком книг"""
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        """Метод возвращает идентификатор для добавления новой книги в библиотеку"""
        if not self.books:  # Если книг нет в списке
            return 1
        else:  # Если книги есть
            return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """Метод возвращает индекс книги"""
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


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

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
