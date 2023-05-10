#multiple return
def my_division(x, y):
    return int(x/y), x%y

#default argument
def my_division_def(x, y=5):
    return int(x/y), x%y

#variable length argument
def info(student_ID, *var):
    print("ID: " + student_ID)
    if len(var) > 0:
        print(var[0])
    if len(var) >= 1:
        print(var[1])

print(my_division(24, 16))
print(my_division_def(24))
info("1905003", "Dipta", "101")
