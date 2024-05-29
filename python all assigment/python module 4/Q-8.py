# Q-8 Write a python program to find the longest words

def find_longest_words(text):
    words = text.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words

text = "Python is a powerful and versatile programming language used for various purposes."
longest_words = find_longest_words(text)
print("Longest words in the text:", longest_words)
