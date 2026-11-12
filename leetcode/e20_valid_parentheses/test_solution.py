import pytest

from leetcode.e20_valid_parentheses.solution import is_valid


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("", True),
        ("))", False),
    ],
)
def test_is_valid(s, expected):
    assert is_valid(s) == expected
