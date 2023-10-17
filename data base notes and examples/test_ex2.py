"""
import pytest

@pytest.fixture
def numders():
    a = 10
    b = 20
    c = 30
    return [a,b,c]

def test_m1(numbers):
    x=15
    assert numbers[0]==x
"""



def test_func_sample():
    a = 2
    b = 2
    assert a==b
