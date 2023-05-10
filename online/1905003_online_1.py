import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 1

x = np.arange(-1, 2, 0.1)
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

def find_root(xL, xU, max_error, max_iteration, count):
    error = 100
    temp = 0
    while(error > max_error):
        xR = (xU * f(xL) - xL * f(xU)) / (f(xL) - f(xU))
        
        count += 1
        if(count != 1):
            error = abs(100 * (xR - temp) / xR)
            print(f"{count}\t\t{error}")
        else:
            print(f"{count}\t\t---")
            
        if(f(xR) * f(xL) > 0):
            xL = xR
        elif(f(xR) * f(xL) < 0):
            xU = xR
        
        temp = xR
    return xR

print("\nRoot: ", find_root(1, 2, 0.05, 50, 0))
    