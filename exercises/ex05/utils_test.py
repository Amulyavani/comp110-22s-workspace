"""For each functions (only_evens, sub, concat), define at least 3x unit test functions"""

__author__ = "730407531"


from utils import only_evens, sub, concat


def test_only_evens_single_item() -> None:
    input: list[int] = [35]
    assert only_evens(input) == []


def test_only_evens_empty() -> None:
    input: list[int] = []
    assert only_evens(input) == []


def test_only_evens_many() -> None:
    input: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(input) == [2, 4, 6]


def test_sub_empty() -> None:
    a_list: list[int] = []
    start: int = 2
    end: int = 5
    assert sub(a_list, start, end) == []


def test_sub_single() -> None:
    a_list: list[int] = [35]
    start: int = 2
    end: int = 5
    assert sub(a_list, start, end) == []


def test_sub_many() -> None:
    a_list: list[int] = [10, 20, 30, 40, 50, 60]
    start: int = 2
    end: int = 5
    assert sub(a_list, start, end) == [30, 40, 50]


def test_concat_empty() -> None:
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_single() -> None:
    first_list: list[int] = [1]
    second_list: list[int] = [2]
    assert concat(first_list, second_list) == [1, 2]


def test_concat_many() -> None:
    first_list: list[int] = [1, 2, 3, 4, 5]
    second_list: list[int] = [6, 7, 8, 9, 10]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]