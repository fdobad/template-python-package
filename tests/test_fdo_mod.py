#!python3
import pytest
from fdo_mod import fdo_module
from numpy import all


def test_fdo_mod_happy():
    # using it without arguments should work
    assert fdo_module.main() == 0, "fdo_module.main() should return 0"
    # test case january month goes back to 12
    assert all(
        fdo_module.surround_year_month(2000, 1)
        == [
            (1999, 12),
            (2000, 1),
            (2000, 2),
        ]
    ), "fdo_module.surround_year_month(2000, 1) should return [(1999, 12), (2000, 1), (2000, 2)]"
    # test case december month goes forward to 1
    assert all(
        fdo_module.surround_year_month(2000, 12)
        == [
            (2000, 11),
            (2000, 12),
            (2001, 1),
        ]
    ), "fdo_module.surround_year_month(2000, 12) should return [(2000, 11), (2000, 12), (2001, 1)]"


def test_fdo_mod_fail():
    with pytest.raises(TypeError):
        fdo_module.surround_year_month(2000.0, 1)
    with pytest.raises(TypeError):
        fdo_module.surround_year_month(2000.0, 1.0)
    with pytest.raises(ValueError):
        fdo_module.surround_year_month(2000, -1)
