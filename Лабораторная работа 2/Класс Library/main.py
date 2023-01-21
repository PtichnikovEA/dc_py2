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


# TODO написать класс Book
class Book:
    """
    Создание и подготовка к работе объекта "Book"
    :param id: Идентификатор книги
    :param name: Название книги
    :param pages: Количество страниц в книге
    Примеры:
    >>> book_book = Book(1, 'test_name', 10)  # инициализация экземпляра класса
    """
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        if pages > 0:
            self.pages = pages
        else:
            raise ValueError("Количество страниц должно быть больше нуля")

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id_}, name=\'{self.name}\', pages={self.pages})'


# TODO написать класс Library
class Library:
    """
    Создание и подготовка к работе объекта "SmartLamp"
    :param books: Список книг
    Примеры:
    >>> library = Library()  # инициализация экземпляра класса
    """
    def __init__(self, books: list[Book] = []):
        self.books = books

    def get_next_book_id(self):
        """
        Функция которая возвращает id следующей книги
        :return: Возвращает id следующей книги
        Примеры:
        >>> library = Library()
        >>> library.get_next_book_id()
        1
        """
        if len(self.books) > 0:
            return self.books[-1].id_ + 1
        else:
            return 1

    def get_index_by_book_id(self, id_):
        """
        Функция возвращающая индекс книги в списке,
        который хранится в атрибуте экземпляра класса.
        :return: Возвращает индекс книги в списке,
        который хранится в атрибуте экземпляра класса.
        Примеры:
        >>> library = Library()
        >>> library.get_index_by_book_id(1):
        ValueError: Книги с запрашиваемым id не существует
        """
        book = list(filter(lambda element: element.id_ == id_, self.books))
        if len(book) > 0:
            return self.books.index(book[0])
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
