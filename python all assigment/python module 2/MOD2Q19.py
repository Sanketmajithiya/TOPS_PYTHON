"""Q.19 Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string."""

def not_poor (str1):
    Snot = str1. find('not')
    
    spoor = str1.find('poor')
    
    if spoor > Snot and Snot > 0 and spoor > 0:
        str1 = str1.replace(str1[Snot:(spoor+4)],'GOOD')
        return str1
    else:
        return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is  poor!'))
     