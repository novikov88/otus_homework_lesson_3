"""You can get acquainted with the markers in the pytest.ini file, if there is no marker, then the AT category test"""
import pytest

from src.Figure import Figure


@pytest.mark.smoke
def test_check_square_from_base_class(default_square):
    assert isinstance(default_square, Figure)


@pytest.mark.smoke
def test_check_square_from_base_class(default_rectangle):
    assert isinstance(default_rectangle, Figure)


@pytest.mark.smoke
def test_check_square_from_base_class(default_triangle):
    assert isinstance(default_triangle, Figure)


@pytest.mark.smoke
def test_check_square_from_base_class(default_circle):
    assert isinstance(default_circle, Figure)


def test_check_any_class_from_base_class(default_class_not_belonging_to_figure):
    assert not isinstance(default_class_not_belonging_to_figure, Figure)
