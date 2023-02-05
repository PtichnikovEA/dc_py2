import doctest

if __name__ == "__main__":
    # Write your solution here

    class Phone:
        """
        Создание и подготовка к работе объекта "Phone"
        :param id: Идентификатор телефона
        :param number: Номер телефона
        Примеры:
        >>> phone_phone = Phone('first', 98356152)  # инициализация экземпляра класса
        """

        def __init__(self, id_: str, number: int):
            if type(id_) != str:
                raise TypeError('Id must be str')
            self.id = id_
            if type(number) != int:
                raise TypeError('Number must be int')
            self.number = number
            self.busy = False

        def call_begin(self, number: int):
            """
            Функция начала звонка
            :param number: Вызываемый номер
            :return: Возвращает состояние звонка
            Пример:
            >>> phone = Phone('first', 98356152)
            >>> phone.call_begin(98356151)
            True
            """
            if type(number) != int:
                raise TypeError('Number must be int')
            if self.busy:
                return False
            self.busy = True
            return True

        def call_end(self):
            """
            Функция завершения звонка
            :return: Возвращает состояние получилось ли выполнить функцию
            Примеры:
            >>> phone = Phone('first', 98356152)
            >>> phone.call_begin(98356151)
            True
            >>> phone.call_end()
            True
            """
            if self.busy:
                self.busy = False
                return True
            else:
                return False

        def __str__(self):
            return f'Phone {self.id}, number: {self.number}'

        def __repr__(self):
            return f'{self.__class__.__name__}({self.id},{self.number})'


    class CellPhone(Phone):
        """
        Создание и подготовка к работе объекта "CellPhone"
        :param id: Идентификатор телефона
        :param number: Номер телефона
        :param model: Модель телефона
        Примеры:
        >>> cell_phone = CellPhone('first', 98356152, 'YotaPhone')  # инициализация экземпляра класса
        """

        def __init__(self, id_: str, number: int, model: str):
            super().__init__(id_, number)
            if type(model) != str:
                raise TypeError('Model must be str')
            self.model = model
            self.signal_strength = 1.0

        def get_signal_strength(self):
            new_signal_strength = 1.0
            # get info from telecommunication tower to new_signal_strength
            self.signal_strength = new_signal_strength
            return self.signal_strength

        def call_begin(self, number: int):
            """
            Функция начала звонка
            :param number: Вызываемый номер
            :return: Возвращает состояние звонка
            Примеры:
            >>> cell_phone = CellPhone('first', 98356152, 'YotaPhone')
            >>> cell_phone.call_begin(98356151)
            True
            """
            if type(number) != int:
                raise TypeError('Number must be int')
            signal_strength = self.get_signal_strength()
            if signal_strength < 0.3:
                return False
            if self.busy:
                return False
            self.busy = True
            return True

        def __str__(self):
            return f'CellPhone {self.id}, number: {self.number}, model: {self.model}'

        def __repr__(self):
            return f'{self.__class__.__name__}({self.id},{self.number},{self.model})'


    doctest.testmod()
    pass
