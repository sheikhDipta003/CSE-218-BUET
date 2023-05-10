class Student:
    student_count = 0   #static variable

    def __init__(self, id, name):   #similar to constructors in C++/Java
        self.name = name    #member variable
        self.id = id        #another member variable
        Student.student_count += 1
    
    def show_count():
        print("Total number of students: ", Student.student_count)
    
    def show_info(self):
        print("ID: ", self.id, "; Name: ", self.name)

def func():
    print("Do something")

#Every Python module has it’s __name__ defined and if this is ‘__main__’, it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
# If you import this script as a module in another script, the __name__ is set to the name of the script/module.
# Python files can act as either reusable modules, or as standalone programs.
# if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
if __name__=="__main__":
    dipta = Student("1905003", "Sheikh Intiser Uddin Dipta")
    somebody = Student("1905123", "xyz")

    del Student.student_count   #In python, we can dynamically delete or create any attribute of any object of a class

    Student.show_count()    #To call a function using the classname, "self" must not be passed to that function
    dipta.show_info()
    somebody.show_info()

