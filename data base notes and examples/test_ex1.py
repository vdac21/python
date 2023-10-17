import pytest

@pytest.fixture
def numders():
    a = 10
    b = 20
    c = 30
    return [a,b,c]

def test_m1(numbers):
    x=10
    assert numbers[0]==x
