"""You can get acquainted with the markers in the pytest.ini file, if there is no marker, then the AT category test"""
import pytest

from src.Rectangle import Rectangle


@pytest.mark.smoke
def test_check_rectangle_from_own_class(default_rectangle):
    assert isinstance(default_rectangle, Rectangle)


@pytest.mark.mat
def test_area_calculation_rectangle_check(default_rectangle):
    assert default_rectangle.area == 200


@pytest.mark.mat
def test_perimeter_calculation_rectangle_check(default_rectangle):
    assert default_rectangle.perimeter == 60


# zero data tests
def test_zero_area_rectangle_calculation_check(zero_rectangle):
    assert zero_rectangle.area == 0


def test_zero_perimeter_rectangle_calculation_check(zero_rectangle):
    assert zero_rectangle.perimeter == 0


# negative tests
@pytest.mark.xfail
@pytest.mark.parametrize('test_input', [-1, -99])
def test_creation_rectangle_less_than_zero(test_input):
    with pytest.raises(ValueError) as exc_info:
        rectangle = Rectangle(test_input, test_input)
    assert str(exc_info.value) == 'Значение не может быть отрицательным'


@pytest.mark.xfail
@pytest.mark.parametrize('test_data', ['a', (1, 3), ['test'], {'one': 1, 2: 'two'}])
def test_creation_rectangle_not_a_number(test_data):
    with pytest.raises(ValueError) as exc_info:
        rectangle = Rectangle(test_data, test_data)
    assert str(exc_info.value) == 'Значение не является числом'


# check add_area
def test_add_area_rectangle_with_square(default_square):
    rectangle = Rectangle(10, 20)
    assert rectangle.add_area(default_square) == 300


def test_add_area_rectangle_with_triangle(default_triangle):
    rectangle = Rectangle(10, 20)
    assert rectangle.add_area(default_triangle) == 284.0


def test_add_area_rectangle_with_circle(default_circle):
    rectangle = Rectangle(10, 20)
    assert rectangle.add_area(default_circle) == 514.1592653589794


@pytest.mark.xfail
def test_add_area_rectangle_with_other_object(default_class_not_belonging_to_figure):
    with pytest.raises(ValueError) as err_info:
        rectangle = Rectangle(10, 20)
        rectangle.add_area(default_class_not_belonging_to_figure)
    assert str(err_info.value) == "ValueError Incorrect class"
