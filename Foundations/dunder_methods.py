""" Dunder Methods

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-29

    Dunder methods are special methods that are used to implement certain
    functionality in Python. They are called dunder methods because they are
    surrounded by double underscores. They are used to implement things like
    the len function, the + operator, and the print function.
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


if __name__ == "__main__":
    example = Example()

    # The print function will call the __str__ method of the object.
    print(example)

    # The len function will call the __len__ method of the object.
    print(len(example))
