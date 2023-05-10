#unordered unique collection of elements
set_example = set()     # empty set is created
set_example.add(10)
print(set_example)
set_example.add(20)
print(set_example)
set_example.add(20)     # if the element is already present, it will not be repeated
print(set_example)

#casting to a set
list_example = [10, 10, 10, 20, 20, 20, 20, 50, 50]
print(list_example)
print(set(list_example))
print(list_example)

print(9.01==9)

