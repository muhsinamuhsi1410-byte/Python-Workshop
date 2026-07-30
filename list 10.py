#Find the frequency of each element

list=[1,2,3,3,3,3,2,4,5,6,6,6,6,6]
new=[]
for i in list:
    if i not in new:
        new.append(i)
        print(i,"=",list.count(i))