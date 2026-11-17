import pytest

from leetcode.m34_find_first_and_last_position.solution import search_range


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([2, 2], 3, [-1, -1]),
    ],
)
def test_search_range(nums, target, expected):
    assert search_range(nums, target) == expected