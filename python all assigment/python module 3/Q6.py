# Q.6 Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of strings

def check_string(str):
    count = 0
    for string in str:
        if len(string) >=2 and string[0] == string[-1]:
            count +=1
    return count
print(check_string(['aba','pqr','xyz','7777','ioi',])) 




       

