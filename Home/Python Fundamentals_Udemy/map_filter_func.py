def percentage(value):
    return value * 0.20

values_list = [5,10,35,100,1000]

# for number in values_list:
#     print(percentage(number))
for number in map(percentage,values_list):  #map(function_name, list_name)
    print(number)

print(list(map(percentage, values_list)))


def even_numbers(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"

print(list(map(even_numbers, values_list)))


def odd_numbers(number):
    return (number % 2 == 1)

print(list(filter(odd_numbers,values_list)))    #the function inserted here may return a boolean value, depending on the truth value of which, the expected elements will be filtered from the list


