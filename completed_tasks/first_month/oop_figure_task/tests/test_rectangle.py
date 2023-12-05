import pytest
from completed_tasks.first_month.oop_figure_task.src.rectangle import Rectangle


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize('a, b, resp', [(1, 4, 4), (7, 5, 35)])
def test_rectangle_area_positive(a, b, resp):
    rec = Rectangle(a, b)
    assert rec.get_area() == resp


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize('a, b, resp', [(1, 4, 10), (7, 5, 24)])
def test_rectangle_perimeter_positive(a, b, resp):
    rec = Rectangle(a, b)
    assert rec.get_perimeter() == resp


@pytest.mark.regress
@pytest.mark.xfail(strict=True, raises=ValueError)
@pytest.mark.parametrize('a, b', [(0, 4), (7, -1), (None, None)])
def test_rectangle_area_negative(a, b):
    Rectangle(a, b)
