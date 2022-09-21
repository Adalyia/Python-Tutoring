""" Scope

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Scope in the context of programming refers to the visibility of variables.
    Variables may be declared anywhere, and thus have different levels of visibility.
    Variables declared outside any classes, functions, or loops are called global variables.
    Global variables are visible everywhere in the program.
    Variables declared inside a class, function, or loop are called local variables.
    Local variables are only visible inside the class, function, or loop they are declared in.
"""

x = 5  # This is a global variable, visible to all functions, classes, and loops within the program

if __name__ == "__main__":
    print(x)  # Prints 5, x is visible here as it's defined at the global scope

    def test():
        # This is a local variable
        # It is only visible inside the function
        y = 2
        print(y)

        print(x)  # Prints 5, x is visible here as it's defined at the global scope

    # print(y) - This would cause an error, as within the global scope y is undefined
