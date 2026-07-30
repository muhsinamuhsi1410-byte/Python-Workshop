#Count the number of unique words in a sentence

sentence = "cat dog cat bird dog"

words = sentence.split()

print(len(set(words)))