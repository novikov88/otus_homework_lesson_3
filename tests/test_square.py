"""You can get acquainted with the markers in the pytest.ini file, if there is no marker, then the AT category test"""
import pytest

from src.Square import Square


@pytest.mark.smoke
def test_check_square_from_own_class(default_square):
    assert isinstance(default_square, Square)


@pytest.mark.mat
def test_area_calculation_square_check(default_square):
    assert default_square.area == 100


@pytest.mark.mat
def test_perimeter_calculation_square_check(default_square):
    assert default_square.perimeter == 40


# zero data tests
def test_zero_area_square_calculation_check(zero_square):
    assert zero_square.area == 0


def test_zero_perimeter_square_calculation_check(zero_square):
    assert zero_square.perimeter == 0


# negative tests
@pytest.mark.xfail
@pytest.mark.parametrize('test_input', [-1, -99])
def test_creation_square_less_than_zero_square(test_input):
    with pytest.raises(ValueError) as exc_info:
        square = Square(test_input)
    assert str(exc_info.value) == 'Значение не может быть отрицательным'


@pytest.mark.xfail
@pytest.mark.parametrize('test_input_not_a_number', ['a', (1, 3), ['test'], {'one': 1, 2: 'two'}])
def test_creation_square_not_a_number(test_input_not_a_number):
    with pytest.raises(ValueError) as exc_info:
        square = Square(test_input_not_a_number)
    assert str(exc_info.value) == 'Значение не является числом'


# check add_area
def test_add_area_square_with_rectangle(default_rectangle):
    square = Square(10)
    assert square.add_area(default_rectangle) == 300


def test_add_area_square_with_triangle(default_triangle):
    square = Square(10)
    assert square.add_area(default_triangle) == 184.0


def test_add_area_square_with_circle(default_circle):
    square = Square(10)
    assert square.add_area(default_circle) == 414.1592653589793


@pytest.mark.xfail
def test_add_area_square_with_other_object(default_class_not_belonging_to_figure):
    with pytest.raises(ValueError) as err_info:
        square = Square(10)
        square.add_area(default_class_not_belonging_to_figure)
    assert str(err_info.value) == "ValueError Incorrect class"
