class Hotel:
    """
    Базовым классом является отель
    """
    def __init__(self, name: str, stars: int, location: str):
        """
        Инициализация атрибутов отеля

        :param name: Название отеля.
        :param stars: Количество звезд отеля (1-5).
        :param location: Местоположение отеля.
        """
        self.name = name
        self.stars = stars
        self.location = location

    def __str__(self) -> str:
        """
        Строковое представление объекта отеля.

        :return: Строка с информацией об отеле.
        """
        return f"Отель {self.name}, {self.stars} звезд, располагается {self.location}"

    def __repr__(self) -> str:
        """
        Формальное строковое представление объекта отеля.

        :return: Форматированная строка.
        """
        return f"Hotel(name='{self.name}', stars={self.stars}, location='{self.location}')"

    def book_room(self) -> str:
        """
        Бронирование номера в отеле.

        :return: Сообщение о бронировании.
        """
        return f"Номер успешно забронирован в {self.name}."

class Hostel(Hotel):
    """
    Дочерний класс для "Hotel", объектом является "Hostel"
    """
    def __init__(self, name: str, stars: int, location: str, capacity_room: int):
        """
        Инициализация атрибутов хостела

        :param name: Название хостела.
        :param stars: Количество звезд хостела (1-5).
        :param location: Местоположение хостела.
        :param capacity_room: Вместимость комнаты.
        """
        super().__init__(name, stars, location)
        self.__capacity_room = capacity_room

    def get_capacity_room(self) -> int:
        """
        Получает вместимость общей комнаты.

        :return: Вместимость общей комнаты.
        """
        return self.__capacity_room

    def __str__(self) -> str:
        """
        Строковое представление объекта хостела.

        Переопределяет метод базового класса, чтобы включить вместимость комнаты.

        :return: Строка с информацией о хостеле.
        """
        return super().__str__() + f", вместимость комнаты: {self.__capacity_room}"

    def __repr__(self) -> str:
        """
        Формальное строковое представление объекта хостела.

        Переопределяет метод базового класса для добавления информации о вместимости.

        :return: Форматированная строка для отладки.
        """
        return f"Hostel(name='{self.name}', stars={self.stars}, location='{self.location}', capacity_room={self.__capacity_room})"

    def book_room(self) -> str:
        """
        Бронирование кровати в комнате.

        Метод перегружен для специфической логики бронирования в хостеле.
        В отличие от базового класса, бронируется не номер, а кровать.

        :return: Сообщение о бронировании.
        """
        return f"Кровать успешно забронирована в {self.name}."

class ResortHotel(Hotel):
    """
    Дочерний класс для "Hotel", объектом является "ResortHotel"
    """
    def __init__(self, name: str, stars: int, location: str, excursions_available: bool):
        """
        Инициализация атрибутов резорт-отеля.

        :param name: Название резорт-отеля.
        :param stars: Количество звезд резорт-отеля (1-5).
        :param location: Местоположение резорт-отеля.
        :param excursions_available: Наличие экскурсий.
        """
        super().__init__(name, stars, location)
        self.__excursions_available = excursions_available

    def __str__(self) -> str:
        """
        Строковое представление объекта резорт-отеля.

        Переопределяет метод базового класса для добавления информации о наличии экскурсий.

        :return: Строка с информацией о резорт-отеле.
        """
        excursion_info = "с экскурсиями" if self.__excursions_available else "без экскурсий"
        return super().__str__() + f", {excursion_info}"

    def __repr__(self) -> str:
        """
        Формальное строковое представление объекта резорт-отеля.

        Переопределяет метод базового класса для добавления информации о наличии экскурсий.

        :return: Форматированная строка для отладки.
        """
        return f"ResortHotel(name='{self.name}', stars={self.stars}, location='{self.location}', excursions_available={self.__excursions_available})"

    def book_room(self) -> str:
        """
        Бронирование номера в резорт-отеле.

        Метод перегружен для добавления информации о наличии экскурсий.

        :return: Сообщение о бронировании.
        """
        return f"Номер успешно забронирован в {self.name} с учетом наличия экскурсий."

if __name__ == "__main__":
    hostel = Hostel("Хостел", 3, "Москва", 11)
    print(hostel)
    print(hostel.book_room())

    resort_hotel = ResortHotel("Resort", 5, "Египет", True)
    print(resort_hotel)
    print(resort_hotel.book_room())
