from completed_tasks.oop_figure_task.src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        self.sides = (side_a, side_b, side_c)
        self.check_params(*self.sides)
        for side in self.sides:
            if not sum(self.sides) - side > side:
                raise ValueError("Cумма длин каждых двух сторон должна быть больше длины третьей стороны.")

    def get_area(self):
        return sum(self.sides) / 2

    def get_perimeter(self):
        return sum(self.sides)
