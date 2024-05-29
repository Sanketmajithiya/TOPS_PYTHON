# Q.54 How can you pick a random item from a range? 

import random
my_range = range(1, 1000)  
random_item = random.choice(list(my_range))
print("Random item from the range:", random_item)
