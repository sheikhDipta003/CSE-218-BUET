list_example = ["one", 2, 3.1416]
print(list_example)
print(list_example[0])
print(list_example[:])  #just like strings, we can slice lists
print(list_example)

#concatenation
colors = ['red', 'blue', 'green']
new_colors = ['orange', 'purple', 'grey']
more_colors = colors + new_colors
print(more_colors)

#mutability
colors[0] = colors[0].upper()
print(colors)
colors.append('black')
print(colors)
removed_item = colors.pop()
print(colors)
print(removed_item)
colors.pop(1)
print(colors)

#reversal
numbers = [52,10,84,37]
numbers.reverse()
print(numbers)

#sorting
numbers.sort()
print(numbers)
more_colors.sort()
print(more_colors)

