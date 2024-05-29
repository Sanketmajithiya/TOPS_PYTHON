# Q.9 Write a Python function that takes two lists and returns true if they haveat least one common member. 

def common_list(list1, list2):
    for item in list1:
        if item in list2:
            return True
        return False
    
    list1 = [1,2,3,6,5]
    list2 = [4,6,7,8,9]
print(common_list('list1','list2'))






















