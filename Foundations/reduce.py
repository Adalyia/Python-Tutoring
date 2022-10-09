""" Reduce

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-10-09

    The reduce function is used to apply a function to every element in an
    iterable, and then combine the results. It returns the final result.
"""

from functools import reduce


def get_sum(x, y):
    return x + y


def get_product(x, y):
    return x * y


if __name__ == "__main__":
    # The reduce function will apply the get_sum function to every element in
    # the list, and then combine the results.
    result = reduce(get_sum, [1, 2, 3, 4, 5])

    print(result)  # 15

    # The reduce function will apply the get_product function to every element
    # in the list, and then combine the results.
    result = reduce(get_product, [1, 2, 3, 4, 5])  # 1 * 2 * 3 * 4 * 5

    print(result)  # 120
