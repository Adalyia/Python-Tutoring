""" Memoization Demo

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-14

    Memoization is a technique used in dynamic programming where the results of
    function calls are cached in a list or dict. The values themselves are computed
    recursively, and the results are stored in the cache.
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


def m_fib(n: int) -> int:
    """Compute the nth Fibonacci number. Utilizing memoization.

    :param n: The index of the Fibonacci number to return.
    :type n: int
    :return: The nth Fibonacci number.
    :rtype: int
    """
    memo = {}  # Memoization cache {n: fib(n)}

    # Here we compute the nth fibonacci number recursively
    def _fib(i: int) -> int:
        if i in memo:
            return memo[i]
        if i <= 1:
            return i
        else:
            memo[i] = _fib(i - 1) + _fib(i - 2)
            return memo[i]

    return _fib(n)


if __name__ == "__main__":
    # Test a normal fib function without memoization
    start = time.perf_counter()  # Start timer
    out = fib(37)
    print(f"fib(37) = {out}, time = {time.perf_counter() - start:f}s")

    # Test a fib function utilizing memoization
    start = time.perf_counter()  # Start timer
    out = m_fib(37)  # This should be much faster than the previous call
    print(f"fib(37) = {out}, time = {time.perf_counter() - start:f}s")

