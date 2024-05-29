"""Q.20 Write a Python function that takes a list of words and returns the length
of the longest one."""

def longestLength(words):
    res = max(words, key=len)
    print("The longest word is:", res, "and its length is", len(res))

a = ["sanket", "san", "dipak", "surat"]
longestLength(a)
