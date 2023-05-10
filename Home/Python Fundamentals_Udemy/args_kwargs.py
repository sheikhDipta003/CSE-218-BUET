def find_percentage(value1, value2, value3):
    return sum((value1,value2,value3)) * 0.20

print(find_percentage(10, 20, 70))

#args -> stores variable number of arguments as a tuple
def find_percentage(*args):
    print(args)

find_percentage(10, 20, 30, 40, 50)

#kwargs-> stores variable number of arguments as key-value pairs like a dictionary
def pets(**kwargs):
    if 'cat' in kwargs:
        print(f"My cat's name is {kwargs['cat']}")
    else:
        print('No cat name is found')
    
    if 'dog' in kwargs:
        print(f"My dog's name is {kwargs['dog']}")
    else:
        print('No dog name is found')

pets(cat="Luna",dog="Charlie")

#both
def students(*args, **kwargs):
    for key in kwargs:
        for value in args:
            print(f"{value} students need {key}.")

students(53, 34, 46, clothes="shirts", equipment="laptops", food="pizzas")


