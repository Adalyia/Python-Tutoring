""" Conditionals

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Conditionals are used to direct the flow of a program.
    They are essential to programming and allow for the
    comparison of values and the execution of code based on
    the result of the comparison.
"""

if __name__ == "__main__":
    x = 5
    y = 10

    # The basic structure of a conditional is value 1 <operator> value 2
    # The operator can be any of the following:
    #   ==  Equal to
    #   !=  Not equal to
    #   >   Greater than
    #   <   Less than
    #   >=  Greater than or equal to
    #   <=  Less than or equal to
    # The result of the comparison is a boolean value (True or False)

    print(x == y)  # Prints False as x is not equal to y
    print(y > x)  # Prints True as y is greater than x

    # If Statements
    if x == y:
        # This code in this indented block will only be executed if x == y
        # which is presently False. This block will not be executed.
        print("x is equal to y")

    if x != y:
        # This code in this indented block will only be executed if x != y
        # which is presently True. This block will be executed.
        print("x is not equal to y")

    # If-Else Statements
    if x == y:
        # This code in this indented block will only be executed if x == y
        # which is presently False. This block will not be executed.
        print("x is equal to y")
    else:
        # This code in this indented block will only be executed if x != y
        # which is presently True. This block will be executed.
        # Else is very powerful, however it should be used sparingly as it
        # is a catch-all. If you find yourself using else, it is likely that
        # you can use elif instead.
        print("x is not equal to y")

    # If-Elif-Else Statements
    # Elif is short for else if, it is used to add more conditions to an
    # if-else statement. Elif is only executed if the previous condition
    # was not met. So in the below example if x did equal y then the next
    # condition would not be checked at all even if it were valid.
    if x == y:
        # This code in this indented block will only be executed if x == y
        # which is presently False. This block will not be executed.
        print("x is equal to y")
    elif x != y:
        # This code in this indented block will only be executed if x != y
        # which is presently True. This block will be executed.
        print("x is not equal to y")
    elif y > x:
        # This code in this indented block will only be executed if y > x
        # which is presently True. This block will not be executed.
        # While the condition is valid it will not be executed as the
        # previous condition was already found to be valid.
        print("y is greater than x")

    # Conditionals may be combined with other operators to create more
    # complex conditions. The following operators are available:
    #   and  Both conditions must be True
    #   or   Either condition must be True
    #   not  The condition must be False
    #   in   The value must be in the list
    #   not in   The value must not be in the list
    #   is   The value must be the same object
    #   is not   The value must not be the same object
    #   is None   The value must be None
    #   is not None   The value must not be None
    #   is True   The value must be True
    #   is not True   The value must not be True
    #   is False   The value must be False
    #   is not False   The value must not be False
    if x == y and y > x:
        # This code in this indented block will only be executed if x == y
        # which is presently False and y > x which is presently True.
        # This block will not be executed.
        print("x is equal to y and y is greater than x")

    if x == y or y > x:
        # This code in this indented block will only be executed if x == y
        # which is presently False or y > x which is presently True.
        # This block will be executed.
        print("x is equal to y or y is greater than x")

    if not x == y:
        # This code in this indented block will only be executed if x != y
        # which is presently True. This block will be executed.
        print("x is not equal to y")

    if x in [1, 2, 3, 4, 5]:
        # This code in this indented block will only be executed if x is in
        # the list [1, 2, 3, 4, 5]. This block will be executed.
        print("x is in the list [1, 2, 3, 4, 5]")

    if x not in [1, 2, 3, 4, 5]:
        # This code in this indented block will only be executed if x is not
        # in the list [1, 2, 3, 4, 5]. This block will not be executed.
        print("x is not in the list [1, 2, 3, 4, 5]")

