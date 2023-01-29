class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
        self.aswe = 1

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    # Свойства для name и author, чтобы запретить их изменение
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if type(pages) == int:
            if pages >= 0:
                self.pages = pages
            else:
                raise ValueError("Количество страниц должно быть неотрицательной")
        else:
            raise TypeError('Количество страниц должно быть числом')

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if type(duration) == float or int:
            if duration >= 0:
                self.duration = duration
            else:
                raise ValueError("Продолжительность должна быть неотрицательной")
        else:
            raise TypeError('Продолжительность должна быть числом')

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration}"

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.duration})'


if __name__ == '__main__':
    b = PaperBook('Python for professionals', 'Matt Telles', 23)
    b.author = 'Harry Rogers'
    # AttributeError: can't set attribute
    print(b.author)
