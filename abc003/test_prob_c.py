import pytest

from abc186.prob_c import *

@pytest.mark.parametrize(('params', 'expected'), [
    ((2, [1000, 1500]), 1000.0),
    ((5, [2604, 2281, 3204, 2264, 2200, 2650, 2229, 2461, 2439, 2211]), 2820.031250000),
])
def test_main(params, expected):
    k, rates = params
    assert main(k, rates) == expected
