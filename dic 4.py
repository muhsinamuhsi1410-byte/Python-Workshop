#Count the frequency of each character in a string

text="apple"
count={}
for i in text:
    count[i]=text.count(i)
print(count)