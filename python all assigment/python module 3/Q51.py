# Q.51 Write a Python function that checks whether a passed string is palindrome or not.

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
string = "A man, a plan, a canal: Panama"
print(f"'{string}' is {'a palindrome.' if is_palindrome(string) else 'not a palindrome.'}")
