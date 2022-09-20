""" Introductions to Python

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Hello World!

    Python is a scripting, interpreted language that while considered
    high-level is extremely powerful for many applications. Python is
    often the language of choice for data-scientists and for machine
    learning applications. Python is also a great language for rapid
    prototyping and for building web applications.

    Part of being a scripting language is that Python code is executed
    line-by-line. This is in contrast to compiled languages like C++ or
    Java where the code is compiled into machine code before execution.
    One of the implications of this is that loose code is run whenever
    files are imported/ran.

    This is why we have the following if statement at the bottom of this
    file. This if statement checks if the file is being run directly or
    if it is being imported. If the file is being run directly, then the
    code within the if statement is executed. If the file is being
    imported, then the code within the if statement is not executed.

    This serves as good practice for writing Python code. It allows us to
    write code that is only executed when the file is run directly, and
    not when the file is imported. This is essentially the equivalent to
    the main function in C++ or Java.
"""

if __name__ == "__main__":
    # The print function is used to print to the console and takes any
    # number of arguments. The arguments are separated by a space when
    # printed.

    print("Hello, World!")

    print("Hello,", "World!")

    # These two examples are identical in function.
