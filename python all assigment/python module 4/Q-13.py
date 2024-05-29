# Q.13 Explain Exception handling? What is an Error in Python? 
"""
Exception handling in Python is a mechanism to deal with errors that occur during program execution.
 It allows you to handle both expected and unexpected errors gracefully, preventing your program from crashing.

try: This is the block of code where you anticipate an error might occur. You place the code that you want to 
monitor inside the try block.

except: This block is executed if an exception occurs within the corresponding try block.
 You can specify the type of exception to catch, or you can catch all exceptions by using a generic except block.

else: This block is executed if no exceptions occur in the try block. It is optional.

finally: This block is always executed, regardless of whether an exception occurred or not. 
It is useful for cleaning up resources, such as closing files or releasing locks. It is also optional.
"""
"""
print("Hello, world!")
x = 10  # Missing colon causes a syntax error

Exceptions (Runtime Errors): These occur during the execution of the program and are not detected by the Python interpreter during parsing. Exceptions are typically caused by factors like invalid user input, unexpected conditions, file not found, division by zero, etc. Exception handling mechanisms are used to handle these runtime errors gracefully and prevent the program from crashing.

Example:try:
    result = 10 / 0  # Division by zero
except ZeroDivisionError:
    print("Cannot divide by zero!")

"""