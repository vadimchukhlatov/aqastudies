import pytest
from completed_tasks.first_month.oop_figure_task.src.circle import Circle


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize('a, resp', [(4, 50.26548245743669), (5, 78.53981633974483)])
def test_rectangle_area_positive(a, resp):
    rec = Circle(a)
    assert rec.get_area() == resp


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize('a, resp', [(4, 25.132741228718345), (7, 43.982297150257104)])
def test_rectangle_perimeter_positive(a, resp):
    rec = Circle(a)
    assert rec.get_perimeter() == resp


@pytest.mark.regress
@pytest.mark.xfail(strict=True, raises=ValueError)
@pytest.mark.parametrize('a', [0, -1, None])
def test_rectangle_negative(a):
    Circle(a)
