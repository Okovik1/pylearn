##TypeCasting = the process of converting a variable from one data type to another
#              str(), int(), float(), bool()

name = "Viktoriia"
age=28
gpa=5.4
is_student=True
type(name)
print(type(is_student))
gpa=int(gpa)
print(gpa)

age=float(age)
print(age)

age=str(age)
print(type(age))

# if not empty will be True , if "" then False
name=bool(name)
print(name)