"""Unit tests for Calculator.subtract()."""
from app.calculator import Calculator

def test_subtraction():
    """subtracts positive and negative numbers correctly"""
    calc = Calculator()
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(-5, -2) == -3
