#convert a tuple into list,append an element  and convert it back

num=(10,20,30)
new=list(num)
new.append(40)
num=tuple(new)
print(num)