"""Unit tests for Calculator.divide()."""
import pytest
from app.calculator import Calculator

def test_division():
    """divides numbers and raises on divide-by-zero"""
    calc = Calculator()
    assert calc.divide(9, 3) == 3
    assert calc.divide(-12, 4) == -3
    with pytest.raises(ValueError):
        calc.divide(1, 0)
