def discount(value):
    return value - (value * 0.30)

print(discount(100))

#lambda expression comes in handy if we want to use a function only once
discount = lambda value: value - (value * 0.30)
print(discount(100))


#using lambda expression with a map
numbers = [10,23,40,57,60,100]
print( list(map(lambda value: value - (value * 0.30), numbers)) )

#using lambda expression with filter
#writing a boolean function to be converted to a lambda expression
def even_number(number):
    return number%2==0

for x in filter(lambda number: number%2==0, numbers):
    print(x, end=" ")


