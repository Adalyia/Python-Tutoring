""" List, Dict, Set, and Tuple Comprehension

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Comprehension is a way to create lists, dictionaries, sets, and tuples in a single line of code.
    It's most useful for skipping the use of a for loop
"""

if __name__ == "__main__":
    # The general format is as follows: <item> for <item> in <iterable> if <condition>
    my_list = [i for i in range(5)]  # Creates a list of the numbers 0 through 4

    my_dict = {i: i for i in range(5)}  # Creates a dictionary with the numbers 0 through 4 as keys and values

    my_set = {i for i in range(5)}  # Creates a set of the numbers 0 through 4

    my_tuple = (i for i in range(5))  # Creates a tuple of the numbers 0 through 4

    # Try to avoid very long comprehension expressions as these are often harder to read and understand than
    # a for loop. If you find yourself writing a comprehension expression that is more than 80 characters long,
    # consider using a for loop instead.
