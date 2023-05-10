import numpy as np
import matplotlib.pyplot as plt

Day = []
Stock_index = []
with open("stock.txt") as file:
    lines = [line.strip() for line in file]
    Day = [float(d.split()[0]) for d in lines if d != lines[0]]
    Stock_index = [float(ind.split()[1]) for ind in lines if ind != lines[0]]

def f(x):
    return Stock_index[Day.index(x)]

def fL2(x):
    n = len(Day)
    diff = []
    points = []
    for i in range(0, n):
        if(Day[i] >= x):
            c = '+'
        else:
            c = '-'
        diff.append((abs(Day[i]-x), c))
    
    diff.sort()

    for i in range(0, 3):
        if(diff[i][1]== '+'):
            points.append(diff[i][0] + x)
        else:
            points.append(x - diff[i][0])
    
    points.sort()

    b_0 = f(points[0]) / ((points[0] - points[1]) * (points[0] - points[2]))
    b_1 = f(points[1]) / ((points[1] - points[0]) * (points[1] - points[2]))
    b_2 = f(points[2]) / ((points[2] - points[0]) * (points[2] - points[1]))

    result = b_0 * (x - points[1]) * (x - points[2]) + b_1 * (x - points[0]) * (x - points[2]) + b_2 * (x - points[0]) * (x - points[1])
    return result

def fL3(x):
    n = len(Day)
    diff = []
    points = []
    for i in range(0, n):
        if(Day[i] >= x):
            c = '+'
        else:
            c = '-'
        diff.append((abs(Day[i]-x), c))
    
    diff.sort()

    for i in range(0, 4):
        if(diff[i][1]== '+'):
            points.append(diff[i][0] + x)
        else:
            points.append(x - diff[i][0])
    
    points.sort()

    b_0 = f(points[0]) / ((points[0] - points[1]) * (points[0] - points[2]) * (points[0] - points[3]))
    b_1 = f(points[1]) / ((points[1] - points[0]) * (points[1] - points[2]) * (points[1] - points[3]))
    b_2 = f(points[2]) / ((points[2] - points[0]) * (points[2] - points[1]) * (points[2] - points[3]))
    b_3 = f(points[3]) / ((points[3] - points[0]) * (points[3] - points[1]) * (points[3] - points[2]))

    result = b_0 * (x - points[1]) * (x - points[2]) * (x - points[3]) + b_1 * (x - points[0]) * (x - points[2]) * (x - points[3]) + b_2 * (x - points[0]) * (x - points[1]) * (x - points[3]) + b_3 * (x - points[0]) * (x - points[1]) * (x - points[2])
    return result

X = float(input())
print(fL3(X))
print("Absolute Relative Approximate Error = " , abs((fL3(X) - fL2(X)) / fL3(X)) * 100)

plt.plot(Day, Stock_index)
plt.axis([0.0, 200.0, -2.0, 2.0])
plt.xlabel('days')
plt.ylabel('stock_index')
plt.title('Closing index of DSE of different days')
plt.annotate("point-1", (X, fL3(X)), arrowprops=dict(facecolor='black'))
plt.grid()
plt.show()
