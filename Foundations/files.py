""" Reading files

    Author(s): Emily Cohen (github.com/Adalyia)
    Date: 2022-10-10

    This snippet shows how to read files in Python. There are two ways to read
    files in Python. The first way is to use the open function. The open
    function will open a file and return a file object. The file object can be
    used to read the file. The second way is to use the with statement. The with
    statement will open a file and return a file object. The file object can be
    used to read the file. The with statement will automatically close the file
    when it is done reading the file.

    The open function has the following parameters:
    - file: The path to the file to open.
    - mode: The mode to open the file in. The default mode is 'r' which means
            read-only. The other modes are 'w' which means write-only, 'a' which
            means append-only, 'r+' which means read and write, and 'w+' which
            means write and read.
    - encoding: The encoding to use when reading the file. The default encoding
                is 'utf-8'.

    The file object has the following methods:
    - read: Reads the entire file and returns the contents as a string.
    - readline: Reads the next line in the file and returns the contents as a
                string.
    - readlines: Reads the entire file and returns the contents as a list of
                strings. Each string in the list is a line in the file.
    - write: Writes the given string to the file.
    - writelines: Writes the given list of strings to the file. Each string in
                the list will be written to a new line in the file.
    - close: Closes the file.
"""

if __name__ == "__main__":
    # Here we are using the open function to open the file  as well as
    # a context manager to open the file. The context manager will automatically
    # close the file when it is done reading the file. This is the preferred
    # way to open files.
    with open("classes.py", "r") as file:  # Open the file in read-only mode. The default mode is 'r'.
        # Read the entire file.
        contents: str = file.read()
        print(contents)
