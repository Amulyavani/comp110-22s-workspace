"""For each functions (only_evens, sub, concat), define at least 3x unit test functions."""

__author__ = "730407531"


from utils import only_evens, sub, concat


def test_only_evens_single_item() -> None:
    """Given that only_evens list is a single item, return an empty list."""
    input: list[int] = [35]
    assert only_evens(input) == []


def test_only_evens_empty() -> None:
    """Given that only_evens list is empty, return an empty list."""
    input: list[int] = []
    assert only_evens(input) == []


def test_only_evens_many() -> None:
    """Given that only_evens list has many integers, return only the evens."""
    input: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(input) == [2, 4, 6]


def test_sub_empty() -> None:
    """Given that sub list is empty, return an empty list."""
    a_list: list[int] = []
    start: int = 2
    end: int = 5
    assert sub(a_list, start, end) == []


def test_sub_single() -> None:
    """Given that a_list is a single item, return an empty list."""
    a_list: list[int] = [35]
    start: int = 2
    end: int = 5
    assert sub(a_list, start, end) == []


def test_sub_many() -> None:
    """Given that the parameter lists have many integers, return only the ones within the bounds of the parameters start and end."""
    a_list: list[int] = [10, 20, 30, 40, 50, 60]
    start: int = 2
    end: int = 5
    assert sub(a_list, start, end) == [30, 40, 50]


def test_concat_empty() -> None:
    """Given that parameter lists are empty, return an empty list."""
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_single() -> None:
    """Given that first_list and second_list are moth single numbers, return a concatenated list of the two parameters."""
    first_list: list[int] = [1]
    second_list: list[int] = [2]
    assert concat(first_list, second_list) == [1, 2]


def test_concat_many() -> None:
    """Given that the concat list has many integers, return a concatenated list of the integers."""
    first_list: list[int] = [1, 2, 3, 4, 5]
    second_list: list[int] = [6, 7, 8, 9, 10]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]