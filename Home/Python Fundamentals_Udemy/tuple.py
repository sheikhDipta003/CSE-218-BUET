my_tuple = ('a', 'b', 'c', 'd')
print(type(my_tuple), "\nlength = ", len(my_tuple))

my_tuple = (1, "two", 3.1416, 4, '6.673', 4, 4, -10)
print(my_tuple[-1])
print(my_tuple.count(4))
print(my_tuple.index(4))

#immutability
my_list = ['one', 'two', 'three']
my_list[1] = my_list[1].upper()         #lists are mutable
print(my_list)

my_tuple = ('one', 'two', 'three')
# my_tuple[1] = my_tuple[1].upper()       #error; tuples are immutable
# print(my_tuple)

