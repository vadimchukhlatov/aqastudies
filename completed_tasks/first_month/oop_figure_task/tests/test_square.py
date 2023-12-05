import pytest
from completed_tasks.first_month.oop_figure_task.src.square import Square


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize('a, resp', [(4, 16), (5, 25)])
def test_rectangle_area_positive(a, resp):
    rec = Square(a)
    assert rec.get_area() == resp


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize('a, resp', [(4, 16), (7, 28)])
def test_rectangle_perimeter_positive(a, resp):
    rec = Square(a)
    assert rec.get_perimeter() == resp


@pytest.mark.regress
@pytest.mark.xfail(strict=True, raises=ValueError)
@pytest.mark.parametrize('a', [0, -1, None])
def test_rectangle_negative(a):
    Square(a)
