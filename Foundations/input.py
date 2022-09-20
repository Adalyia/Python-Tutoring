""" Input

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Retrieving input from the user is a common task in programming.
    In Python, we can use the input() function to retrieve input from the user.
    The input() function will return a string containing the user's input.
"""

if __name__ == "__main__":
    # Here we're using the input() function to retrieve input from the user
    # The result will always be a string however, so for example if we wanted to use the input as a number
    # We would need to convert it to an integer or float
    # We can do this using the int() or float() functions
    # If we try to convert a string that isn't a number, we'll get an error
    # For example, if we try to convert the string "Hello, World!" to an integer
    # We'll get an error because "Hello, World!" isn't a number
    user_input = input("Enter some text: ")

    # We can use the print() function to print the user's input
    print(user_input)
