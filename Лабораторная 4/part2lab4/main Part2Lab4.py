from typing import List, Union

class Animal:
    """
    Базовый класс для животных.

    Атрибуты:
        name (str): Имя животного.
        species (str): Вид животного (например, млекопитающее, птица, рептилия).
    """

    def __init__(self, name: str, species: str):
        """Инициализирует экземпляр класса Animal."""
        self.name = name
        self.species = species

    def make_sound(self) -> str:
        """Издает звук, характерный для животного данного вида."""
        return "Generic animal sound"

    def __str__(self) -> str:
        """Возвращает строковое представление животного."""
        return f"{self.__class__.__name__}(name='{self.name}', вид='{self.species}')"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта для отладки."""
        return f"{self.__class__.__name__}(name='{self.name}', вид='{self.species}')"


class Dog(Animal):
    """
    Класс для собак, наследуемый от Animal.
    """

    def __init__(self, name: str):
        """Инициализирует экземпляр класса Dog."""
        super().__init__(name=name, species="Собака")

    def make_sound(self) -> str:
        """Перегружает метод make_sound для возврата "Гав!"."""
        return "Гав!"


class Cat(Animal):
    """
    Класс для кошек, наследуемый от Animal.
    """

    def __init__(self, name: str):
        """Инициализирует экземпляр класса Cat."""
        super().__init__(name=name, species="Кошка")

    def make_sound(self) -> str:
        """Перегружает метод make_sound для возврата "Мяу!"."""
        return "Мяу!"


if __name__ == '__main__':
    murka = Cat(name="Мурка")
    bim = Dog(name="Бим")

    print(murka)
    print(murka.make_sound())

    print(bim)
    print(bim.make_sound())