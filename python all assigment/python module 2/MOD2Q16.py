"""Q.16 Write a Python program to count the occurrences of each word in a
given sentence """

strl = input("enter the sentence")
strl = strl. split()
i= 0
count = 0
while i< len(strl):
    count = 0
    for j in strl:
        if strl[i]==j:
            count += 1
    print((strl[i]),"The occurance is :",count)
    i += 1        
    