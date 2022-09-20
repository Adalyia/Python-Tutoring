""" Sets

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Sets are a collection of values. They are similar to lists, but they are unordered and unique.
    Sets are mutable, meaning they can be changed after they are created.
    Sets are unordered, meaning the order of the values is not preserved.
    Sets are not indexed, meaning each value in the set does not have an index.
    Sets are iterable, meaning they can be used in a range-based for loop.
    Sets are not subscriptable, meaning they cannot be indexed using square brackets.
    Sets are not hashable, meaning they cannot be used as keys in a dict.
    Sets are unique, meaning they cannot contain duplicate values.
    Sets are not homogeneous, meaning they can contain values of different types.
"""

if __name__ == "__main__":
    # Here we've created a set, it contains both integers and strings
    # The set is mutable however, so we can change the values in the
    # set after it is created, add new values, and also remove them.
    # But, the values are unique. Meaning we cannot have two of the same value in a set.
    my_set = {1, 2, 3, 4, 5, "six", "seven", "eight", "nine", "ten"}

    # We can add a value to the set using the add method
    my_set.add("eleven")  # This adds the value "eleven" to the set

    # We can also remove a value from the set using the remove method
    my_set.remove("ten")  # This removes the value "ten" from the set

    # We can also remove a value from the set using the discard method
    my_set.discard("nine")  # This removes the value "nine" from the set

    # We can also remove a value from the set using the pop method
    my_set.pop()  # This removes a random value from the set

    # We can also remove all values from the set using the clear method
    my_set.clear()  # This removes all values from the set

