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
# TODO написать класс Book


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
