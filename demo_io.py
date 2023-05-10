a = input("Enter something: ")
print(a)

with open("input.txt", "r") as fp:
    #text = fp.input()
    i = 0
    for line in fp:
        print("printing line: ", i, line)
        i += 1

fp.close()
