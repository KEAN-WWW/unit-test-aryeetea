"""Unit tests for Calculator.multiply()."""
from app.calculator import Calculator

def test_multiplication():
    """multiplies numbers including zero and negatives"""
    calc = Calculator()
    assert calc.multiply(7, 0) == 0
    assert calc.multiply(-3, 5) == -15
