import pytest
from main import suma, resta, division


def test_suma():
    assert suma(1, 1) == 2
    assert suma(1, 2) == 3


def test_suma_exception():
    with pytest.raises(TypeError):
        suma("asdfasdfa", 1)


def test_resta():
    assert resta(1, 1) == 0
    assert resta(1, 2) == -1


def test_division():
    assert division(10,2) == 5
    assert division(15,3) == 5
