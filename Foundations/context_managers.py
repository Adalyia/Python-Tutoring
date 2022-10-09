""" Context Managers

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-29

    Context managers are a way to manage resources in Python. They are used to
    ensure that resources are properly managed, and that they are cleaned up
    when they are no longer needed. They are used in conjunction with the
    with statement.
"""


class Example:
    def __init__(self):
        print("Example.__init__")

    def __enter__(self):
        print("Example.__enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Example.__exit__")

    @staticmethod
    def do_something():
        print("Example.do_something")


if __name__ == "__main__":
    # The with statement is used to manage resources. It will call the
    # __enter__ method of the object, and then call the __exit__ method
    # when the with block is exited.
    with Example() as example:
        example.do_something()
