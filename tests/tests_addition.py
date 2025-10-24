"""Unit tests for Calculator.add()."""
from app.calculator import Calculator

def test_addition():
    """adds positive and negative numbers correctly"""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-4, -6) == -10
