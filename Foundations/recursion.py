""" Recursion

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Recursion breaks larger problems down into smaller ones.
    This is accomplished by calling the same function within itself.
    However, recursion requires a base case to prevent an infinite loop.
    The base case is the condition that will stop the function from calling itself.
    If the base case is not met, the function will call itself again.
    This will continue until the base case is met, at which point the function will return.

    Recursion should be used very carefully as it can be very easy to create an infinite loop.
    Thorough testing is required to ensure that the base case is met.
    Python has a maximum recursion depth of 1000, so if the base case is not met the function will crash.
    However, this can be changed by setting the sys.setrecursionlimit() function. (Warning, very not advised)
"""


def sum_r(n):
    """ This is an example of a recursive function that sums the numbers 1 to n
    The base case is n == 0, which will stop the function from calling itself
    """
    if n == 0:
        return 0
    else:
        """ This is the recursive call
        The function calls itself with a different argument
        The function will continue to call itself until the base case is met
        
        In this case, the function will add the value of n to sum_r(n - 1) and
        continue to call itself until n == 0.
        """
        return n + sum_r(n - 1)


if __name__ == "__main__":
    print(sum_r(10))  # Prints 55, this test is relatively fast.
