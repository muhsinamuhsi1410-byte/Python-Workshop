#Create a list of 10 numbers and print the largest number

list=[10,20,30,40,50,25,70,78,90,100]
largest=list[0]
for i in list:
    if i>largest:
        largest=i
print("Largest numbers=",largest)