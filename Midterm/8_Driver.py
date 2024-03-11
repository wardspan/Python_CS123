age = 16

def can_drive(age):
    if age > 15 and age <= 18:
        print("You can get a learner's permit")
    elif age > 18:
        print("You can drive!")
    else:
        print("You can't drive yet")

can_drive(age)
age = 18
print(age)
can_drive(age)
age = 12
print(age)
