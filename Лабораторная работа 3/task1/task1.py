class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    # Свойства для name и author, чтобы запретить их изменение
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError('Attribute name is read-only')

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        raise AttributeError('Attribute author is read-only')


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if type(value) == int:
            if value >= 0:
                self.pages = value
            else:
                raise ValueError("Количество страниц должно быть неотрицательной")
        else:
            raise TypeError('Количество страниц должно быть числом')

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if type(value) == float or int:
            if value >= 0:
                self.duration = value
            else:
                raise ValueError("Продолжительность должна быть неотрицательной")
        else:
            raise TypeError("Продолжительность должна быть числом")

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.duration})'


if __name__ == '__main__':
    b = PaperBook('Python for professionals', 'Matt Telles', 23)
    print(b.pages)
    b.author = 'Harry Rogers'
    # AttributeError: Attribute author is read-only
    print(b.author)
