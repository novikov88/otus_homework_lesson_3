"""You can get acquainted with the markers in the pytest.ini file, if there is no marker, then the AT category test"""
import pytest

from src.Triangle import Triangle


@pytest.mark.smoke
def test_check_triangle_from_own_class(default_triangle):
    assert isinstance(default_triangle, Triangle)


@pytest.mark.mat
def test_area_triangle_rectangle_check(default_triangle):
    assert default_triangle.area == 84.0


@pytest.mark.mat
def test_perimeter_calculation_triangle_check(default_triangle):
    assert default_triangle.perimeter == 42


# negative tests
@pytest.mark.xfail
@pytest.mark.parametrize('test_input', [0, -1, -100])
def test_creation_triangle_less_than_zero_first(test_input):
    with pytest.raises(ValueError) as exc_info:
        triangle = Triangle(test_input, 14, 15)
    assert str(exc_info.value) == 'Треугольник не может быть создан по заданным параметрам'


@pytest.mark.xfail
@pytest.mark.parametrize('test_input', [0, -1, -100])
def test_creation_triangle_less_than_zero_second(test_input):
    with pytest.raises(ValueError) as exc_info:
        triangle = Triangle(13, test_input, 15)
    assert str(exc_info.value) == 'Треугольник не может быть создан по заданным параметрам'


@pytest.mark.xfail
@pytest.mark.parametrize('test_input', [0, -1, -100])
def test_creation_triangle_less_than_zero_third(test_input):
    with pytest.raises(ValueError) as exc_info:
        triangle = Triangle(13, 14, test_input)
    assert str(exc_info.value) == 'Треугольник не может быть создан по заданным параметрам'


@pytest.mark.xfail
@pytest.mark.parametrize('test_data', ['a', (1, 3), ['test']])
def test_creation_triangle_not_a_number(test_data):
    with pytest.raises(ValueError) as exc_info:
        triangle = Triangle(test_data, test_data, test_data)
    assert str(exc_info.value) == 'Значение не является числом'


# check add_area
def test_add_area_triangle_with_square(default_square):
    triangle = Triangle(13, 14, 15)
    assert triangle.add_area(default_square) == 184


def test_add_area_rectangle_with_rectangle(default_rectangle):
    triangle = Triangle(13, 14, 15)
    assert triangle.add_area(default_rectangle) == 284.0


def test_add_area_triangle_with_circle(default_circle):
    triangle = Triangle(150, 150, 150)
    assert triangle.add_area(default_circle) == 10056.945057933914


@pytest.mark.xfail
def test_add_area_rectangle_with_other_object(default_class_not_belonging_to_figure):
    with pytest.raises(ValueError) as err_info:
        triangle = Triangle(150, 150, 150)
        triangle.add_area(default_class_not_belonging_to_figure)
    assert str(err_info.value) == "ValueError Incorrect class"
