# Q.48 Write a Python function to calculate the factorial of a number (a nonnegative integer) 


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
num = 5
print("Factorial of", num, "is:", factorial(num))

