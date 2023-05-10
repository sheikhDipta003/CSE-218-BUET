import numpy as np
import matplotlib.pyplot as plt
import math

h = np.arange(0, 10, 0.1)
def f(h):
    return 37.7*h*h - 3.1416*(h**3) - 15
def f_(h):
    return 75.4*h - 9.425*(h**2)

plt.plot(h, f(h))
plt.axis([0.0, 10, -15, 900])
plt.xlabel('Height of the Oil Level in the tank')
plt.ylabel('Volume of Oil in the Tank')
plt.grid()
plt.show()

#intial guess -> 1
h1 = -1
def find_root(h, max_error, count):
    error = 100
    while(error > max_error):
        h1 = round(h - f(h) / f_(h), 5)
        count += 1
        if count!=1:
            error = round(abs(100 * (h1 - h) / h1), 5)
            print(f"{count}\t\t{h1}\t\t{error}")
        else:
            print(f"{count}\t\t{h1}\t\t---")
        h = h1


find_root(1, 0.05, 0)
