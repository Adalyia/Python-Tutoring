""" Dictionaries

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Dictionaries are a collection of key-value pairs. They are similar to HashMaps in Java.
    Dictionaries are mutable, meaning they can be changed after they are created.
    Dictionaries are ordered, meaning the order of the key-value pairs is preserved. (Python 3.7+)
    Dictionaries are unique, meaning they cannot contain duplicate keys. They can contain duplicate values, however.
    Dictionaries are subscriptable, meaning they can be indexed using square brackets. (By their keys)
    Dictionaries are not hashable, meaning they cannot be used as keys in a dict.
    Dictionaries are not homogeneous, meaning they can contain keys and values of different types.
"""

if __name__ == "__main__":
    # Here we've created a dictionary, it contains both integers and strings in its values.
    # The dictionary is mutable however, so we can change the values in the
    # dictionary after it is created, add new key-value pairs, and also remove them.
    my_dict = {
        "Manufacturer": "Ford",
        "Model": "Mustang",
        "Year": 1964,
        "Color": "Red",
        "Price": 5000,
    }

    # We can access the values in the dictionary using their keys
    print(my_dict["Manufacturer"])  # Prints Ford
    print(my_dict["Model"])  # Prints Mustang

    # Here I'd like to add a new key-value pair to the dictionary
    # We can do this using the same syntax as accessing a value
    my_dict["Mileage"] = 10000  # This adds the key-value pair "Mileage": 10000 to the dictionary

    # We can also change the value of a key-value pair
    my_dict["Year"] = 1965  # This changes the value of the key "Year" to 1965

    # We can also remove a key-value pair from the dictionary using the del keyword
    del my_dict["Price"]  # This removes the key-value pair "Price": 5000 from the dictionary
