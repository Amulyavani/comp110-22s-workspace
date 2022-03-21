"""Exercise 05 'list' Utility Functions."""

__author__ = "730407531"


def only_evens(input: list[int]) -> list[int]:
    """Given a list of ints, only_evens should return a list containing only the elements of the input list that were even."""
    new_list: list[int] = []
    if len(input) < 1:
        return new_list
    for item in input:
        if len(input) > 1:
            if item % 2 == 0:
                new_list.append(item)
    return new_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, a start index, and an end index, sub should generate a list which is a subset of the given list between the start index and the end index - 1."""
    returned_list: list[int] = []
    i: int = 0
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if len(a_list) == 0:
        return returned_list
    if start > len(a_list):
        return returned_list
    if end <= 0:
        return returned_list
    i = start
    while i < end:
        returned_list.append(a_list[i])
        i += 1
    return returned_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Given two Lists of ints, concat should generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    combined: list[int] = []
    for item in first_list:
        combined.append(item)
    for item in second_list:
        combined.append(item)
    return combined