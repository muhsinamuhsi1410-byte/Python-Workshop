#Reverse a list without using reverse() or slice()

list=[1,2,3,4,5,6,7,8,9]
new=[]
for i in list:
    new.insert(0,i)
print(new)