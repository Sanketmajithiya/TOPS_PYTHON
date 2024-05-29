# Q.15 When will the else part of try-except-else be executed? 
"""In Python, the else block in a try-except statement is executed when no exception occurs in the try block. 
If an exception occurs, the except block is executed, and the else block is skipped.
try:
    # Code that may raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Code to execute if no exception occurs
    
"""
''' The else part is executed when no exception occurs. '''


print("start")
try:
    a = int(input("Enter something: "))
except ValueError:
    print("Please enter only digit")
except NameError:
    print("Please define variable a")
except Exception as e:
    print(f"ERROR : {e}")
else:
    print(a  + 10)

print("end")