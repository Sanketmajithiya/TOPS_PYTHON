"""Q.5 What is the purpose continue statement in python?


In Python, the continue statement is used within loops (such as for loops or while loops) to skip the rest of the code inside the loop for the current iteration, and to proceed with the next iteration of the loop.

The purpose of the continue statement is to alter the flow of the loop based on certain conditions. When the continue statement is encountered, the remaining statements within the loop for that iteration are skipped, and the loop proceeds with the next iteration, if any.
example:-
"""
for i in range(1, 11):
    if i == 3:
        continue
    print(i)


