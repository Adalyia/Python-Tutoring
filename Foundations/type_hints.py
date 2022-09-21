""" Type Hinting

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Type hinting is a way to specify the type of variable or function parameter.
    It's useful for documenting code and for static type checking.
    Type hinting is optional, but it's recommended practice for both convenience and readability.
    Type hinting is denoted by a colon followed by the type of the variable or function parameter.
"""

if __name__ == "__main__":
    x: int = 5  # This is an integer, we've specified the type as int using type hinting

    # A major advantage to type hinting is that it allows for static type checking, which reduces the likelihood of bugs
    # x = "Hello, World!" - This would cause an error with static type checking, as x is defined as an int, not a string

    # Another advantage is that it allows for IDEs to provide autocomplete suggestions (I recommend PyCharm)


    def test(y: int) -> int:
        # This function takes an integer as a parameter and returns an integer
        # We've specified the type of the parameter and the return value using type hinting
        return y + 1
