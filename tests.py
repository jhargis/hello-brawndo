import pytest

def func(x):
    return x + 1

def test_answer_true():
    assert func(4) == 5

def test_answer_true2():
    assert func(5) == 6

