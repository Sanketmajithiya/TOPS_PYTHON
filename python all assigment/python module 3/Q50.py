# Q.50  Write a Python function to check whether a number is perfect or not. 

def is_perfect(number):
    return number > 0 and sum(i for i in range(1, number) if number % i == 0) == number

number = 28
print(f"{number} is {'a perfect number.' if is_perfect(number) else 'not a perfect number.'}")

