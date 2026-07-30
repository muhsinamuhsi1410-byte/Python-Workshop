#Sort a dictionary by its values

student = {"Rahul":90, "Asha":85, "Riya":95}

print(sorted(student.items(), key=lambda x: x[1]))