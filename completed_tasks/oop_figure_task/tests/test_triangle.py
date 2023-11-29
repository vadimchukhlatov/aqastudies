import pytest
from completed_tasks.oop_figure_task.src import Triangle


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize('a, b, c, resp', [(1, 4, 4, 4.5), (7, 5, 11, 11.5)])
def test_triangle_area_positive(a, b, c, resp):
    rec = Triangle(a, b, c)
    assert rec.get_area() == resp


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize('a, b, c, resp', [(7, 4, 10, 21), (2, 5, 6, 13)])
def test_triangle_perimeter_positive(a, b, c, resp):
    rec = Triangle(a, b, c)
    assert rec.get_perimeter() == resp


@pytest.mark.regress
@pytest.mark.xfail(strict=True, raises=ValueError)
@pytest.mark.parametrize('a, b, c', [(0, 4, 2), (7, -1, 3), (7, -1, None), (1, 2, 9)])
def test_triangle_area_negative(a, b, c):
    Triangle(a, b, c)
