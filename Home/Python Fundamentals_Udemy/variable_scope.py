var = "Global scope"

def variable_scope():
    #var = "Enclosing scope"

    def another_func():
        #var = "Local scope"
        print("variable scope is ", var)
    
    another_func()

variable_scope()

#LEGB -> Local, Enclosing, Global, Built-in
#First, python will start finding a variable in local scope
#If not found, it will look in the enclosing scope, and so on upto built-in scope.

cat = "Luna"

def cat_name(cat):
    #global cat
    print(f"My cat's name is {cat}")    #prints "Luna"
    cat = "Chloe"
    print(f"Now my cat's name is {cat}")    #"Chloe"

cat_name(cat)
print(cat)
