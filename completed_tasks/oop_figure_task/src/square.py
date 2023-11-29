from completed_tasks.oop_figure_task.src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        self.check_params(side_a)
        super().__init__(side_a, side_a)
