from completed_tasks.oop_figure_task.src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.check_params(side_a, side_b)
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
