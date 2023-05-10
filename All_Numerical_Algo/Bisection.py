import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, 12, 0.1)
plt.plot(x, x**3 - 18*(x**2) + 475.2)
plt.axis([0, 12, -390, 480])
plt.grid()
plt.show()

#From the graph, the root seems to lie in the interval (6.2, 6.5)
#Therefore, the value of the root is approximately 6.4
#The initial values of the lower and upper bounds are taken to be 6.2 and 6.5


#returns the value of f(x)
def f(x):
    #return x**3 - 18 * (x**2) + 475.2
    return 1.65*pow(10, -12) * math.exp(x*pow(10, -3)/25.8) +x - 5


#returns approximate value of the root of f(x) within 'expected_error' and 'max_iteration' number of iterations
def find_root(lower_bound, upper_bound, expected_error, max_iteration):
    count = 0                   #tracks count of current number of iterations
    error = 100                 #current 'Absolute Relative Approximate Error'
    temp = -1                   #temporary variable to store the mid_value of previous iteration
    mid_value = lower_bound     #assigning arbitrary initial value to mid_value
    
    if (f(lower_bound) * f(upper_bound) > 0):
        return None
    elif (f(lower_bound) == 0 and f(upper_bound) != 0):
        return lower_bound
    elif (f(lower_bound) != 0 and f(upper_bound) == 0):
        return upper_bound
    else:
        while(error > expected_error and count < max_iteration):
            mid_value = (lower_bound + upper_bound) / 2
            count += 1

            if(count > 1):          #error cannot be calculated for the first iteration since there is no previous mid_value
                error = (abs(mid_value - temp) / mid_value) * 100

            if(f(lower_bound) * f(mid_value) < 0):
                upper_bound = temp = mid_value
                continue
            elif (f(lower_bound) * f(mid_value) > 0):
                lower_bound = temp = mid_value
                continue
            else:
                return mid_value
        
    return round(mid_value, 5)


# Similar to the find_root() function,
# except two print statements have been added inside the while loop within an if-else condition
# and another print statement outside of the outermost if-elif chain.
def show_error(lower_bound, upper_bound, expected_error, max_iteration):
    count = 0
    error = 100
    temp = -1
    mid_value = lower_bound

    print("No. of iteration\tAbsolute Relative Approx. Error")      #addition-1
    
    if (f(lower_bound) * f(upper_bound) > 0):
        return None
    elif (f(lower_bound) == 0 and f(upper_bound) != 0):
        return lower_bound
    elif (f(lower_bound) != 0 and f(upper_bound) == 0):
        return upper_bound
    else:
        while(error > expected_error and count < max_iteration):
            mid_value = (lower_bound + upper_bound) / 2
            count += 1

            if(count > 1):
                error = (abs(mid_value - temp) / mid_value) * 100
                print(f"{count}\t\t\t{round(error,3)}")             #addition-2
            else:
                print(f"{count}\t\t\t---")                          #addition-3

            if(f(lower_bound) * f(mid_value) < 0):
                upper_bound = temp = mid_value
                continue
            elif (f(lower_bound) * f(mid_value) > 0):
                lower_bound = temp = mid_value
                continue
            else:
                return mid_value
        
    return round(mid_value, 5)


print("\nroot = ", find_root(0.6, 0.8, 0.5, 100))
#show_error(6.2, 6.5, 0.5, 20)
print()
