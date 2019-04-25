import pytest

def func(x):
    return x + 1

def test_answer_true():
    assert func(4) == 5

def test_answer_false():
    assert func(3) == 5
