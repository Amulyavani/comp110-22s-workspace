"""Dictionary related utility functions."""

__author__ = "730407531"

from csv import DictReader

# Define your functions below


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a `list` of rows, each row represented as `dict[str, str]."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(path, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(rows_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = rows_table[0]
    for column in first_row:
        result[column] = column_values(rows_table, column)
    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a column-based table wiith only the first parameter rows of data for each column."""
    result: dict[str, list[str]] = {}

    for column in column_table:
        a: list[str] = column_table[column]
        empty: list[str] = []
        for item in a:
            if len(empty) < rows:
                empty.append(item)
        result[column] = empty
    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for column in names:
        result[column] = column_table[column]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined.."""
    result: dict[str, list[str]] = {}

    for column in table_one:
        result[column] = table_one[column]
    for column in table_two:
        if column in result[column]:
            result[column] += table_two[column]
        else:
            result[column] = table_two[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result