""" Functions

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Functions are used to compartmentalize code into reusable blocks.
    Functions are useful when you want to perform the same action multiple times.
    They are also useful when you want to perform an action on multiple values.
"""


def my_function():
    """ This is an example function
    We use the keyword def to define a function followed by the name of the function and a set of parentheses
    The parentheses are used to pass arguments to the function
    The function body is indented after the parentheses
    The function body is the code that will be executed when the function is called
    """
    print("Hello, World!")


def my_function_with_args(arg1, arg2):
    """ This is an example function that takes arguments
    The arguments are passed to the function in the parentheses
    The arguments are separated by commas
    """
    print(arg1, arg2)


def my_function_with_return(arg1, arg2):
    """ This is an example function that returns a value
    The return keyword is used to return a value from the function
    """
    return arg1 + arg2


if __name__ == "__main__":
    # We call the function by using the function name followed by a set of parentheses and any required arguments
    my_function()  # Prints "Hello, World!"
    my_function_with_args("Hello", "World!")  # Prints "Hello World!"

    # We can also use the return keyword to return a value from the function
    # We can then use the value in our code
    x = my_function_with_return(1, 2)
    print(x)  # Prints 3

