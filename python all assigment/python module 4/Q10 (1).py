"""Q.10 Write a Python program to count the frequency of words in a file. """
def word_frequency(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        words = file.read().split()

        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    print("Word Fre : ")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

filename = 'new_file.txt'  
word_frequency(filename)
