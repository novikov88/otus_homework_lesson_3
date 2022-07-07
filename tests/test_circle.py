"""You can get acquainted with the markers in the pytest.ini file, if there is no marker, then the AT category test"""
import pytest

from src.Circle import Circle


@pytest.mark.smoke
def test_check_circle_from_own_class(default_circle):
    assert isinstance(default_circle, Circle)


@pytest.mark.mat
def test_area_calculation_circle_check(default_circle):
    assert default_circle.area == 314.1592653589793


@pytest.mark.mat
def test_perimeter_calculation_circle_check(default_circle):
    assert default_circle.perimeter == 62.83185307179586


# zero data tests
def test_zero_area_circle_calculation_check(zero_circle):
    assert zero_circle.area == 0


def test_zero_perimeter_circle_calculation_check(zero_circle):
    assert zero_circle.perimeter == 0


# negative tests
@pytest.mark.xfail
@pytest.mark.parametrize('test_input', [-1, -99])
def test_creation_circle_less_than_zero(test_input):
    with pytest.raises(ValueError) as exc_info:
        circle = Circle(test_input)
    assert str(exc_info.value) == 'Значение не может быть отрицательным'


@pytest.mark.xfail
@pytest.mark.parametrize('test_input_not_a_number', ['a', (1, 3), ['test'], {'one': 1, 2: 'two'}])
def test_creation_circle_not_a_number(test_input_not_a_number):
    with pytest.raises(ValueError) as exc_info:
        circle = Circle(test_input_not_a_number)
    assert str(exc_info.value) == 'Значение не является числом'


# check add_area
def test_add_area_circle_with_rectangle(default_rectangle):
    circle = Circle(10.1)
    assert circle.add_area(default_rectangle) == 520.4738665926948


def test_add_area_square_with_triangle(default_triangle):
    circle = Circle(10.10)
    assert circle.add_area(default_triangle) == 404.4738665926948


def test_add_area_circle_with_square(default_circle):
    circle = Circle(0.010)
    assert circle.add_area(default_circle) == 314.1595795182447


@pytest.mark.xfail
def test_add_area_square_with_other_object(default_class_not_belonging_to_figure):
    with pytest.raises(ValueError) as err_info:
        circle = Circle(1000)
        circle.add_area(default_class_not_belonging_to_figure)
    assert str(err_info.value) == "ValueError Incorrect class"
