""" Q.6 Write python program that swap two number with temp variable and without temp variable."""
# 1.Swapping with a temporary variable
def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Example usage:
num1 = 10
num2 = 50
print("Before swapping:", num1, num2)
num1, num2 = swap_with_temp(num1, num2)
print("After swapping:", num1, num2)

# 2.Swapping without a temporary variable
def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b 

# Example usage: 
num1 = 10
num2 = 30
print("Before swapping:", num1, num2)
num1, num2 = swap_without_temp(num1, num2)
print("After swapping:", num1, num2)

