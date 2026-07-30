#Rotate a list to the right by k positions

list=[1,2,3,4,5,6,7,8,9]
k=2
for i in range(k):
    last=list.pop()
    list.insert(0,last)
print(list)