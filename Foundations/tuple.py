""" Tuples

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Tuples are a collection of values. They are similar to lists, but they are immutable.
    Tuples are immutable, meaning they cannot be changed after they are created.
    Tuples are ordered, meaning the order of the values is preserved.
    Tuples are indexed, meaning each value in the tuple has an index.
    Tuples are iterable, meaning they can be used in a range-based for loop.
    Tuples are subscriptable, meaning they can be indexed using square brackets.
    Tuples are not hashable, meaning they cannot be used as keys in a dict.
    Tuples are not unique, meaning they can contain duplicate values.
    Tuples are not homogeneous, meaning they can contain values of different types.
"""

if __name__ == "__main__":
    # Here we've created a tuple, it contains both integers and strings
    # The tuple is immutable however, so we cannot change the values in the
    # tuple after it is created, add new values, or remove them.
    my_tuple = (1, 2, 3, 4, 5, "six", "seven", "eight", "nine", "ten")

    # We can access the values in the tuple using their index
    # Most formats of indexing start at 0, so the first value in the tuple
    # is at index 0, the second at index 1, and so on.
    print(my_tuple[0])  # Prints 1
    print(my_tuple[1])  # Prints 2
    print(my_tuple[2])  # Prints 3



