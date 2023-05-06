# tuple = collections which is ordered and unchangeable
#         used to group together related data

student = ("Denji", 19, "male")

print(student.count("Denji"))
print(student.index("male"))

for x in student:
    print(x)

if "Rai" in student:
    print("Denji is present!")