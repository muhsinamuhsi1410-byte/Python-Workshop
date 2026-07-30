#Find all pairs whose sum equals a target

numbers=[1,2,3,4,5,6,7,8,9,10]
target=5
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==target:
           print(numbers[i],numbers[j])