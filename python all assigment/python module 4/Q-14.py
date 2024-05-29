# Q.14 How many except statements can a try-except block have? Name Some built-in exception classes:
"""A try block can have multiple except statements to handle different types of exceptions that may occur 
within the try block. There's no strict limit to the number of except statements you can have, but typically
 you would handle the specific exceptions that your code may encounter."""

try:
    x = 10 / 0  
    y = int("abc")  
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid conversion!")

    """In this example, the except block following ZeroDivisionError will handle exceptions of type ZeroDivisionError, and the except block following ValueError will handle exceptions of type ValueError.

As for some built-in exception classes in Python, here are a few common ones:

ZeroDivisionError: Raised when division or modulo by zero occurs.
ValueError: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
TypeError: Raised when an operation or function is applied to an object of inappropriate type.
IndexError: Raised when a sequence subscript is out of range.
KeyError: Raised when a dictionary key is not found.
FileNotFoundError: Raised when a file or directory is requested but cannot be found.
IOError: Raised when an I/O operation (such as opening a file) fails.
NameError: Raised when a local or global name is not found.
AttributeError: Raised when an attribute reference or assignment fails.
SyntaxError: Raised when there is a syntax error in the code."""