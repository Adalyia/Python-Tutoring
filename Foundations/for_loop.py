""" For Loops

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    For loops are used to iterate over a collection of values.
    Loops are useful when you want to perform the same action on multiple values.
"""

if __name__ == "__main__":
    # We're using a list of 5 integers as an example
    my_list = [1, 2, 3, 4, 5]

    # Here we're using a for loop to iterate over the list
    # The variable i is the current value in the list
    # This is equivalent to a range-based for loop in Java/C++
    for i in my_list:
        print(i)  # Prints 1, 2, 3, 4, 5

    # Here we're using a for loop to iterate over the list
    # The variable i is the current index in the list
    # This is equivalent in function to a standard for loop, for i = 0; i < len(my_list); i++)
    for i in range(len(my_list)):
        # The advantage here is that we can use i to access the value at the that index in the list
        # Sometimes this is more convenient than using the value directly
        print(my_list[i])  # Prints the value at index i


