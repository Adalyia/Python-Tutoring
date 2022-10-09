""" Map

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-10-09

    The map function is used to apply a function to every element in an
    iterable. It returns an iterator that can be used to access the results.
"""


def double(x):
    return x * 2


if __name__ == "__main__":
    # The map function will apply the double function to every element in the
    # list.
    result = map(double, [1, 2, 3, 4, 5])

    # The result is an iterator that can be used to access the results.
    print(list(result))  # [2, 4, 6, 8, 10]

