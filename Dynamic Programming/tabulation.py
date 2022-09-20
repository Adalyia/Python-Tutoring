""" Tabulation Demo

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-14

    Tabulation is a technique used in dynamic programming where the results of
    function calls are cached in a list or dict. The values themselves are computed
    iteratively, and the results are stored in the cache.
"""

import time


def fib(n: int) -> int:
    """ Compute the nth Fibonacci number.

    :param n: The index of the Fibonacci number to return.
    :return: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def t_fib(n: int) -> int:
    """Compute the nth Fibonacci number. Utilizing tabulation.

    :param n: The index of the Fibonacci number to return.
    :type n: int
    :return: The nth Fibonacci number.
    :rtype: int
    """
    if n <= 1:
        return n

    # Create a list to store the Fibonacci numbers.
    tab = [0] * (n + 1)
    tab[1] = 1

    # Compute the Fibonacci numbers iteratively, storing each in the list.
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]

    return tab[n]


if __name__ == "__main__":
    # Test a normal fib function without tabulation
    start = time.perf_counter()  # Start timer
    out = fib(37)
    print(f"fib(37) = {out}, time = {time.perf_counter() - start:f}s")

    # Test a fib function utilizing tabulation
    start = time.perf_counter()  # Start timer
    out = t_fib(37)  # This should be much faster than the previous call
    print(f"fib(37) = {out}, time = {time.perf_counter() - start:f}s")
