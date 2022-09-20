""" While Loops

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-09-20

    While loops are used to repeat a block of code while a condition is met.
    Loops are useful when you want to perform the same action on multiple values.
"""

if __name__ == "__main__":
    # Here we're using a while loop to print the numbers 1 to 9
    x = 1

    while x <= 10:
        # This is a finite loop, it will run until x is no longer less than or equal to 10
        print(x)
        x += 1

    while True:
        # This is an infinite loop, it will run forever unless we break out of it explicitly
        # break is a keyword that will exit the loop
        # This is useful if we want to exit the loop based on some condition
        # For example, if we wanted to exit the loop if the user entered a specific value
        # We could use an if statement to check the value and break if it matches
        # break

        # continue is a keyword that will skip the rest of the loop and start the next iteration
        # This is useful if we want to skip the rest of the loop based on some condition
        # For example, if we wanted to skip the rest of the loop if the user entered a specific value
        # We could use an if statement to check the value and continue if it matches
        # continue

        # Alternatively within the Python console you can use CTRL+C to kill the script entirely
        print("Hello, World!")
