# Q.63 Write a Python program to returns sum of all divisors of a number .

print("The sum of all divisors of", (lambda n: sum([i for i in range(1, n + 1) if n % i == 0]))(int(input("Enter a number: "))))

