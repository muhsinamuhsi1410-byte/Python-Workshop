#merge 2 list and remove duplicates

list1=[1,2,3,4]
list2=[4,5,1,6]
new=[]
for i in list1+list2:
    if i not in new:
        new.append(i)
print(new)
