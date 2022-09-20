""" Lists

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Lists are exactly that, a list of values.
    Lists are mutable, meaning they can be changed after they are created.
    Lists are ordered, meaning the order of the values in the list is preserved.
    Lists are indexed, meaning each value in the list has an index.
    Lists are iterable, meaning they can be used in a range-based for loop.
    Lists are subscriptable, meaning they can be indexed using square brackets.
    Lists are not hashable, meaning they cannot be used as keys in a dict.
    Lists are not unique, meaning they can contain duplicate values.
    Lists are not homogeneous, meaning they can contain values of different types.
"""

if __name__ == "__main__":
    # Here we've created a list, it contains both integers and strings
    # The list is mutable however, so we can change the values in the
    # list after it is created, add new values, and also remove them.
    my_list = [1, 2, 3, 4, 5, "six", "seven", "eight", "nine", "ten"]

    # We can access the values in the list using their index
    # Most formats of indexing start at 0, so the first value in the list
    # is at index 0, the second at index 1, and so on.
    print(my_list[0])  # Prints 1
    print(my_list[1])  # Prints 2
    print(my_list[2])  # Prints 3

    # Here I'd like to add a value to the end of the list
    # We can do this using the append method
    my_list.append("eleven")  # This adds the value "eleven" to the end of the list

    # We can also add a value to the list at a specific index or change
    # the value at a specific index
    my_list[0] = "one"  # This changes the value at index 0 to "one"

    # We can also remove a value from the list using the remove method
    my_list.remove("ten")  # This removes the value "ten" from the list


