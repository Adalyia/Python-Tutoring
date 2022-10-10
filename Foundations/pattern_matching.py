""" Structural pattern matching in Python 3.10+

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-29

    Structural pattern matching is a new feature in Python 3.10 that allows
    you to match a value against a pattern. If the value matches the pattern,
    then the code in the match block will be executed. If the value does not
    match the pattern, then the code in the match block will not be executed.

    This is similar to switch statements in other languages, however the use
    case isn't quite the same as it doesn't offer a tangible speed increase.
    However, it does offer a more readable syntax and a more concise way of
    writing code. It also allows you to match against multiple patterns at
    once, which is not possible with switch statements.
"""


class Example:
    def __init__(self):
        self._param1: int = 1
        self._param2: int = 2
        self._param3: str = "Hello, World!"
        self._cache = {
            "param1": self._param1,
            "param2": self._param2,
            "param3": self._param3,
        }
        print("Example.__init__")

    def __str__(self):
        return f"Example(param1={self._param1}, param2={self._param2}, " \
               "param3={self._param3})"

    def __len__(self):
        return len(self._cache)

    @property
    def param1(self):
        return self._param1

    @property
    def param2(self):
        return self._param2

    @property
    def param3(self):
        return self._param3


def pattern_match_example(value):
    """
    The match statement will match the value against the pattern. If the value
    matches the pattern, then the code in the match block will be executed.

    Specifically in match statements you can use the following patterns:
    - literals
    - sequences
    - mappings
    - classes
    - wildcards
    - and more

    You can also match against multiple patterns at once using the | operator.

    To match against classes like in the example below you can use the same
    syntax as instantiating a new object. This is equivalent to
    isinstance(value, Example) and value.arg1=x and value.arg2=y and value.arg3=z.
    """
    match value:
        case Example(param1=1, param2=2, param3="Hello, World!") as ex:
            print("Case 1", ex)  # Example(param1=1, param2=2, param3=Hello, World!)
        case Example() as ex:
            print("Case 2", ex)  # Example(param1=?, param2=?, param3=?)
        case _:
            print("Default case")


def old_example(value):
    """
    This is the old way of doing this. It is much more verbose and less
    readable than the new match statement.
    """
    if isinstance(value, Example) and value.param1 == 1 and value.param2 == 2 and value.param3 == "Hello, World!":
        print(value)
    elif isinstance(value, Example):
        print(value)
    else:
        print("Default case")


if __name__ == "__main__":
    example = Example()

    pattern_match_example(example)  # Case 1 Example(param1=1, param2=2, param3=Hello, World!)
    example._param1 = 5
    pattern_match_example(example)  # Case 2 Example(param1=5, param2=2, param3=Hello, World!)

    old_example(example)  # Case 2 Example(param1=5, param2=2, param3=Hello, World!)
    example._param1 = 1
    old_example(example)  # Case 1 Example(param1=1, param2=2, param3=Hello, World!)
