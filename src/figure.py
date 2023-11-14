from abc import ABC, abstractmethod
import math


class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()

    def check_params(self, *params):
        for param in params:
            if type(param) not in (int, float) or param <= 0:
                raise ValueError(f"Невалидное значение - {type(param), param} для класса {self.__class__.__name__}!")
