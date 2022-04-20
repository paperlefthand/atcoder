import pytest

from abc186.prob_c import *

@pytest.mark.parametrize(('nums', 'expected'), [
    ([1, -3, 1, 0], 4),
    ([3, -6, 4, -5, 7], 0),
    ([-1, 4, 3, 2, -5, 4], 8),
])
def test_main(nums, expected):
    assert main(nums) == expected
