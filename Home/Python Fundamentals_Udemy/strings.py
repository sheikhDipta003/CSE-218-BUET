text = "This is a string."

print(text[0:4])    #[start:stop:step] -> 'stop' index is excluded
print(text[8:])     #by skipping the 'stop' index, we can fetch all the characters upto the end
print(text[:7])     #by skipping the 'start' index, we can fetch all the characters from the start till the 'stop' index
print(text[:])      #the entire string can be obtained by doing this
print(text[::1])    #go along the entire string and print every 'step'th character starting from 'start' index
print(text[::-1])   #print the entire string backwards

#string multiplication
string2 = "hi"
string2 *= 5
print(string2)
#string2[0] = 'g'    #error, strings are immutable
#print(string2)

string3 = "Hey everyone!"
print(string3.upper())
print(string3)      #since strings are immutable, the original string is unchanged
string3 = string3.upper()
print(string3)      #but if we reassign the string, it will be definitely changed
print(string3.split())      #by default, splitting will be done based on whitespaces

#string interpolation -> inserting a variable within a string
name = "Dipta"
place = "Chattogram"

print(f'My name is {name} and I was born in {place}')

