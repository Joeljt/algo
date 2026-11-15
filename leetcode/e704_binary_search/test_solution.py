import pytest

from leetcode.e704_binary_search.solution import search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
    ],
)
def test_search(nums, target, expected):
    assert search(nums, target) == expected