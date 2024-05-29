# Q.20 Write python program that user to enter only odd numbers, else will raise an exception

num = (int(input("Enter a odd number only: ")))
if num % 2 == 0:
    raise ValueError(input("you entered even number, enter odd number only: "))
else:
    print("Entered number is Odd.")


















