""" Write a Python program that will return true if the two given integer values are equal or their sum 
    or difference is 5."""

def check_number(a, b):
    print( a == b or abs(a - b) == 5 or a + b == 5 )

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))

result = check_number(num1, num2)
print(result)
