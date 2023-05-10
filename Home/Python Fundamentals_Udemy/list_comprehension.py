name = "Jonathon"
letters = []

# for letter in name:
#     letters.append(letter)
letters = [letter for letter in name]
print(letters)

values = [number for number in range(1, 21)]
print(values)
values = [number for number in range(1,21) if number%2==0]      #we can add if conditions inside list comprehension
print(values)
values = [number if number%2==0 else 'Odd number' for number in range(1,21)]    #if-else conditions
print(values)

#nested for loop in list comprehension
values = []
# for i in [2, 3, 4]:
#     for j in [1, 10, 100]:
#         values.append(i*j)
values = [i*j for i in [2,3,4] for j in [1, 10, 100]]
print(values)


