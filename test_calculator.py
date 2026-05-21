import pytest
from calculator import add, subtract, multiply, divide


# --- add ---
def test_add_positive():
    assert add(3, 4) == 7

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5


# --- subtract ---
def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(7, 0) == 7


# --- multiply ---
def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(9, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6


# --- divide ---
def test_divide_positive():
    assert divide(10, 2) == 5.0

def test_divide_float_result():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(5, 0)

def test_add_by_nagative_reset():
    assert add(12,2) == 14