import pytest

from prob_c import *

def test_gcd():
    assert gcd(6,8) == 2

def test_lcm():
    assert lcm(12, 15) == 60

@pytest.mark.parametrize(('times', 'expected'), [
    ([2,3], 6),
    ([2,5,10,1000000000000000000,1000000000000000000], 1000000000000000000),
])
def test_main(times, expected):
    assert main(times) == expected
