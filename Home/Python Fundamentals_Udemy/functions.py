def is_even(value):
    return value%2==0

def is_even_list(my_list):
    even_numbers = []

    for value in my_list:
        if is_even(value):
            even_numbers.append(value)
        else:
            pass
    
    return even_numbers

returned_list = is_even_list([10, 5, -67, 46, 70, 11, 3])
print(returned_list)

#tuple unpacking with a function
laptops = [('Dell', 800), ('HP', 600), ('Lenovo', 700)]
for laptop, price in laptops:
    print(price-(0.2*price))


#tuple unpacking with functions
exam_points = [('AAA', 80), ('BBB', 67), ('CCC', 91)]

def student_rank(exam_points):
    max_points = 0
    best_student = ''
    for student,points in exam_points:
        if(points > max_points):
            max_points = points
            best_student = student
        else:
            pass
    
    return (best_student, max_points)

name,points = student_rank(exam_points)
print(name," ",points)