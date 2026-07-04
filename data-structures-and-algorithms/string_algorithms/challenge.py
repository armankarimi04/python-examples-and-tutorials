# Use a list comprehension to return a list of all the words in the following list that have more than four characters: 
words = ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]

words2 = [i for i in words if len(i) > 4]

print(words2)