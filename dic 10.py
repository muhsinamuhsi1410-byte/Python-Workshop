#Find the word that appears most frequently in a sentence

sentence = "cat dog cat bird cat dog"

words = sentence.split()

count = {}

for i in words:
    count[i] = words.count(i)

print(max(count, key=count.get))