"""Q.9 Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero."""

def sum_unique(a, b, c):
    if a == b == c:  # If all three values are equal
        return 0
    elif a == b or b == c or a == c:  # If any two values are equal
        return 0
    else:
        return a + b + c

# Test the function
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

result = sum_unique(num1, num2, num3)
print("Sum of unique integers:", result)


