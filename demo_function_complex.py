def reassign(lst):
    lst = [0, 1]
    return lst

def append(lst):
    lst.append(1)

my_list = [0]
my_list = reassign(my_list)
#print(my_list)
append(my_list)
#print(my_list)

# generator example; while working with large data set
def gen_f():
    i = 0
    for j in range(10):
        yield i
        i += 1
        print("Calling ", i)

obj = gen_f()
for i in range(10):
    print(next(obj))

