# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Concert:
    def __init__(self, date: str, artist: str, concert_running_time: float):
        """
        Объектом является "Концерт"

        :param date: Дата проведения концерта.
        :param artist: Исполнитель, выступающий на концерте.
        :param concert_running_time: Продолжительность концерта в часах и минутах.

        :raise ValueError: Если продолжительность концерта меньше или равно нулю, вызовем ошибку

        Пример:
        >>> concert = Concert("12-06-2024", "Stray Kids", 1.5) # инициализация экземпляра класса
        """
        if concert_running_time <= 0:
            raise ValueError("Продолжительность концерта должна быть положительным числом")
        self.date = date
        self.artist = artist
        self.concert_running_time = concert_running_time

    def sell_ticket(self) -> None:
        """
        Продажа билетов на концерт

        Пример:
        >>> concert = Concert("12-06-2024", "Stray Kids", 1.5)
        >>> concert.sell_ticket()  # Должен продать билет
        """
        ...

    def cancel_concert(self) -> None:
        """
        Отмена концерта

        Пример:
        >>> concert = Concert("12-06-2024", "Stray Kids", 1.5)
        >>> concert.cancel_concert()  # Должен отменить концерт
        """
        ...

    def reschedule_concert(self, new_date: str) -> None:
        """
        Перенос концерт на новую дату

        :param new_date: Новая дата концерта в формате 'DD-MM-YYYY'.

        Пример:
        >>> concert = Concert("12-06-2024", "Stray Kids", 1.5)
        >>> concert.reschedule_concert("19-07-2024")  # Должен перенести концерт
        """
        ...

class MusicAlbum:
    def __init__(self, title: str, artist: str, count_of_tracks: int):
        """
        Объектом класса является "MusicAlbum"

        :param title: Заголовок альбома.
        :param artist: Исполнитель альбома.
        :param count_of_tracks: Количество треков в альбоме (должно быть положительным целым числом).

        :raise ValueError: Количество треков не может быть меньше или равно нулю, вызовем ошибку
        Пример:
        >>> album = MusicAlbum("High Road", "LDR", 12)
        """
        if count_of_tracks <= 0:
            raise ValueError("Количество треков должно быть положительным целым числом.")
        self.title = title
        self.artist = artist
        self.tracks = count_of_tracks

    def play_album(self) -> None:
        """
        Проигрывает альбом

        >>> album = MusicAlbum("High Road", "LDR", 12)
        >>> album.play_album()  # Должен начать проигрывание альбома
        """
        ...

    def get_tracklist(self) -> list:
        """
        Возвращает список треков альбома

        :return: Список треков

        >>> album = MusicAlbum("High Road", "LDR", 12)
        >>> album.get_tracklist()  # Показывает список треков
        """
        ...

class Chocolate:
    def __init__(self, brand: str, type_of_chocolate: str, weight: int):
        """
        Объектом класса является "Chocolate"

        :param brand: Бренд шоколада.
        :param type_of_chocolate: Вид шоколада.
        :param weight: Вес шоколада в граммах (должен быть положительным числом).

        :raise ValueError: Если вес шоколада меньше или равно нулю, вызовем ошибку
        Пример:
        >>> chocolate = Chocolate("Kinder", "White", 140)
        """
        if weight <= 0:
            raise ValueError("Вес шоколада должен быть положительным числом.")
        self.brand = brand
        self.type_of_chocolate = type_of_chocolate
        self.weight = weight

    def unwrap(self) -> None:
        """
        Разворачивание обертки шоколада
        >>> chocolate = Chocolate("Kinder", "White", 140)
        >>> chocolate.unwrap()  # Разворачивает шоколад
        """
        ...

    def taste(self) -> str:
        """
        Проба шоколад и описание его вкуса

        :return: Возвращает описание вкуса шоколада.

        >>> chocolate = Chocolate("Kinder", "White", 140)
        >>> chocolate.taste()  # Описывает вкус шоколада
        """
        ...


if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
