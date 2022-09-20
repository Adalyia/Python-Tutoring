""" Types and Variables

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Typing in Python is optional, but it is highly recommended. Python is
    a dynamically typed language, meaning that a variable's type is
    determined at runtime. This is in contrast to statically typed
    languages like C++ or Java where a variable's type is determined
    at compile time. This means that in Python, a variable's type can
    change at any time. This is a powerful feature of Python, but it can
    also lead to bugs if not used correctly.
"""

if __name__ == "__main__":
    # In Python, variables are typed by their assigned value.
    # The type() function is used to get the type of variable.
    # The type of variable can be changed at any time.

    w = True  # w is a boolean, these are the values True and False
    print(w, type(w))  # Prints True <class 'bool'>

    x = 10  # x is an integer, these are whole numbers, positive or negative
    print(x, type(x))  # Prints 10 <class 'int'>

    y = "Hello, World!"  # y is a string, these are sequences of characters
    print(y, type(y))  # Prints Hello, World! <class 'str'>

    z = 10.0  # z is a float, these are numbers with a decimal point
    print(z, type(z))  # Prints 10.0 <class 'float'>

    c = 1j  # c is a complex number, these are numbers with a real and imaginary part
    print(c, type(c))  # Prints 1j <class 'complex'>

    # Python has many built-in types, but it is also possible to create
    # new types. This is done in classes which will be covered later.
