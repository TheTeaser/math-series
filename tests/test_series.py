import pytest
from series.series import *

"""
Tests for Fib and Lucas series:
"""

# Fibonacci test cases:

def test_fibonacci_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_four():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_five():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


# Lucas test cases:

def test_lucas_one():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_two():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_three():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_four():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_five():
    actual = lucas(4)
    expected = 7
    assert actual == expected


# Sum_series test cases:


def test_sum_one():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_tqo():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_three():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_four():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_five():
    actual = sum_series(4,2,3)
    expected = 13
    assert actual == expected