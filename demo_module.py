#from math import ceil
import math
# from demo_oop import Student
# from demo_oop import func
from demo_oop import *

print(math.ceil(5.5))
dipta = Student("1905003", "Sheikh Intiser Uddin Dipta")
somebody = Student("1905123", "xyz")
Student.show_count()    #To call a function using the classname, "self" must not be passed to that function
dipta.show_info()
somebody.show_info()
func()
