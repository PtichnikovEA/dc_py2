# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union, Any
import doctest


class SmartLamp:
    """
    Создание и подготовка к работе объекта "SmartLamp"
    :param state: Состояние
    :param brightness: Яркость
    :param mode: Режим работы
    Примеры:
    >>> lamp = SmartLamp(1, 55, 'disco')  # инициализация экземпляра класса
    """
    def __init__(self, state: Any = 0, brightness: Union[int, float] = 50, mode: str = 'default'):
        self.state = bool(state)
        if not isinstance(brightness, (int, float)):
            raise TypeError("Яркость лампы должна быть типа int или float")
        self.brightness = 0 if brightness < 0 else 100 if brightness > 100 else brightness
        if not isinstance(mode, str):
            raise TypeError("Режим работы должен быть типа str")
        self.mode = mode

    def toggle_state(self) -> bool:
        """
        Функция которая переключает состояние лампы
        :return: Возвращает текущее состояние
        Примеры:
        >>> lamp = SmartLamp(1, 55)
        >>> lamp.toggle_state()
        False
        """
        self.state = not self.state
        return self.state

    def change_brightness(self, brightness: Union[int, float]) -> None:
        """
        Изменение яркости лампы.
        :param brightness: Устанавливаемая яркость
        Примеры:
        >>> lamp = SmartLamp(1, 55)
        >>> lamp.change_brightness(45)
        """
        self.brightness = 0 if brightness < 0 else 100 if brightness > 100 else brightness


class Speakers:
    """
    Создание и подготовка к работе объекта "Speakers"
    :param state: Состояние
    :param volume: Громкость
    Примеры:
    >>> speakers = Speakers(0, 15)  # инициализация экземпляра класса
    """
    def __init__(self, state: Any = 0, volume: Union[int, float] = 10):
        self.state = bool(state)
        if not isinstance(volume, (int, float)):
            raise TypeError("Громкость колонок должна быть типа int или float")
        self.volume = 0 if volume < 0 else 100 if volume > 100 else volume

    def toggle_state(self) -> bool:
        """
        Функция которая переключает состояние колонок
        :return: Возвращает текущее состояние
        Примеры:
        >>> speakers = Speakers(0, 33)
        >>> speakers.toggle_state()
        True
        """
        self.state = not self.state
        return self.state

    def change_volume(self, volume: Union[int, float]) -> None:
        """
        Изменение громкости
        :param volume: Устанавливаемая громкость
        Примеры:
        >>> speakers = Speakers(1, 13)
        >>> speakers.change_volume(17)
        """
        self.volume = 0 if volume < 0 else 100 if volume > 100 else volume


class Room:
    """
    Создание и подготовка к работе объекта "Room"
    :param furniture: Список мебели
    :param doors: Количество дверей
    :param windows: Количество окон
    Примеры:
    >>> room = Room(['chair','bed'], 1, 2)  # инициализация экземпляра класса
    """
    def __init__(self, furniture: list = [], doors: int = 1, windows: int = 0):
        if not isinstance(furniture, list):
            raise TypeError("Список мебели должен быть типа list")
        self.furniture = furniture
        if not isinstance(doors, int):
            raise TypeError("Количество деверей должно быть типа int")
        if doors < 1:
            raise ValueError("Количество деверей должно быть больше 0")
        self.doors = doors
        if not isinstance(windows, int):
            raise TypeError("Количество окон должно быть типа int")
        if windows < 0:
            raise ValueError("Количество окон должно быть положительным")
        self.windows = windows

    def add_furniture(self, item: str) -> list:
        """
        Функция которая добавляет мебель в комнату
        :return: Возвращает список мебели в комнате
        Примеры:
        >>> room = Room(['chair','bed'], 1, 2)
        >>> room.add_furniture('lamp')
        ['chair', 'bed', 'lamp']
        """
        if not isinstance(item, str):
            raise TypeError("Название мебели должно быть типа str")
        self.furniture.append(item)
        return self.furniture

    def add_windows(self, num_windows: int) -> int:
        """
        Добавление окон в комнату
        :param num_windows: Количество добавляемых окон
        Примеры:
        >>> room = Room(['chair','bed'], 1, 2)
        >>> room.add_windows(5)
        7
        """
        if not isinstance(num_windows, int):
            raise TypeError("Количество окон должно быть типа int")
        if num_windows < 0:
            raise ValueError("Количество окон должно быть положительным")
        self.windows = self.windows + num_windows
        return self.windows




if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  #
    pass
