"""11 Write a python program to sum of the first n positive integers. """
def sum_of_positive(n):
    sum = 0
    for i in range(1, n + 1):
        sum +=i
    return sum
n = int(input("enter the value of a : "))
result = sum_of_positive(n)
print(f"sum of positive n value is : {result}")