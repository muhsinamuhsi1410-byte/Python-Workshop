#Reverse a dictionary (swap keys and values)

student = {"Rahul":90, "Asha":85}

new = {}

for key, value in student.items():
    new[value] = key

print(new)