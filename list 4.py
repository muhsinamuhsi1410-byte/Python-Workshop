#Remove duplicate elements without using set

list=[1,2,2,3,3,4,5,6,6,7,8,9,10,10]
new=[]
for i in list:
    if i not in new:
        new.append(i)
        print(i)