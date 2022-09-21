""" Formatting Strings

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    There's a number of ways to format Strings in python.
    The most common way is to use the format() function.
    The format() function is a method of the String class.
    It's used to format a string by replacing placeholders with values.
    This is a direct equivalent to the C#/Java String.Format() function.

    Another way to format strings is to use f-strings.
    f-strings are a new way to format strings in Python 3.6+.
    They are a direct equivalent to the C#/Java $"" string interpolation.
    f-strings are denoted by an f at the beginning of the string.
    The values to be inserted into the string are denoted by curly braces.
"""

x = 5  # This is a global variable, visible to all functions, classes, and loops within the program

if __name__ == "__main__":
    x = "{}, {}!".format("Hello", "World")  # This is a string formatted using the format() function
    x2 = "{0}, {1}!".format("Hello", "World")  # format() also supports positional arguments (0, 1, 2, etc.)
    x3 = "{word1}, {word2}!".format(word1="Hello", word2="World")  # format() also supports keyword arguments

    y = f"{x} I love Python!"  # This is a string formatted using an f-string

    print(x)  # Prints "Hello, World!"

    print(y)  # Prints "Hello, World! I love Python!"

    # Python also allows for code execution within strings as well as actual format changes within strings
    z = f"{0.0500000:.2f}"  # This is an f-string formatted to 2 decimal places
    print(z)  # Prints "0.05"

    # This is an f-string formatted to 2 decimal places and with a comma every 3 digits
    # The comma is added by using a comma in the format specifier
    z2 = f"{1000000.0500000:,.2f}"
    print(z2)  # Prints "1,000,000.05"
