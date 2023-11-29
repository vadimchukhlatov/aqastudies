from completed_tasks.oop_figure_task.src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.check_params(radius)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius
