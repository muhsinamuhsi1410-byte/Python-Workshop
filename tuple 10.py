#remove duplicate values by creating new tuple

tup=(1,2,2,2,3,4,5,5)
new=()
for i in tup:
    if i not in new:
        new=new+(i,)
print(new)