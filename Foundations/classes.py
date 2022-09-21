""" Classes and Objects

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    Classes are used to define the structure of an object.
    Objects are instances of a class.

    int, float, str, list, dict, and tuple are all examples of classes. These are all built-in classes.
    However, in most object-oriented languages we're able to define our own classes.

    Classes are useful for representing real-world objects.
    For example, if we wanted to represent a car in our code, we could define a Car class.
    We could then create multiple Car objects to represent different cars.
"""


class Car:
    def __init__(self, make, model, year):
        """ This is called a constructor method and is called whenever a new instance of the class is created
        The constructor method is used to initialize the attributes of the class and is always named __init__
        The constructor method is always passed self as the first argument
        The constructor method is always passed any other arguments that are required to initialize the class
        The first argument of any method in a class represents the instance of the class, and is usually named self

        :param make: The make of the car
        :param model: The model of the car
        :param year: The year of the car
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        # This is called a string method and is called whenever the class is converted to a string
        return f"{self.year} {self.make} {self.model}"

    def get_make(self):
        """ This is called a method, methods are functions that are defined within a class
        It is common to create getter and setter methods for each attribute of a class
        This is a getter method, it is used to get the value of an attribute
        """
        return self.make

    def set_make(self, make):
        """ This is called a method, methods are functions that are defined within a class
        It is common to create getter and setter methods for each attribute of a class
        This is a setter method, it is used to set the value of an attribute
        """
        self.make = make


if __name__ == "__main__":
    # Here we create an instance of the "Car" class and pass the required arguments to the constructor method
    my_car = Car("Nissan", "Rogue", 2019)

    print(my_car, type(my_car))  # Prints "2019 Nissan Rogue <class '__main__.Car'>"
    print(my_car.get_make())  # Prints "Nissan"

    # We can also create multiple instances of the same class
    my_other_car = Car("Ford", "F-150", 2018)
    print(my_other_car, type(my_other_car))  # Prints "2018 Ford F-150 <class '__main__.Car'>"
