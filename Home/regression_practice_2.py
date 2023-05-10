from math import exp, log
import matplotlib.pyplot as plt

x = []
y = []

with open("data.txt") as file:
    while(True):
        line = file.readline().strip()
        if not line:
            break

        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))

print(x)
print(y)
N = len(x)
#plotting
plt.scatter(x, y, color='red', label='Given data points', marker='o')
plt.legend(loc='upper left')
# plt.plot(x, [f(i, 1, 1) for i in x], color='blue', label='Computed curve')
# plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

summands = ['x^2', 'x', 'xy', 'y', '1']

def sum(summand, n):
    sum = 0
    for i in range(0,n):
        if(summand == 'x^2'):
            sum += x[i]**2
        elif(summand == 'x'):
            sum += x[i]
        elif(summand == 'xy'):
            sum += x[i] * log(y[i])
        elif(summand == 'y'):
            sum += log(y[i])
        elif(summand == '1'):
            sum += 1

    return sum

def f(x, a, b):
    return (a*exp(b*x))

def  GaussianElimination(A,B,pivot=True,showall=True):
    step = 1
    n = len(A)
    roots = [0]*n

    #  reduction to row-echelon form
    while step < n:
        k = step - 1
        if(pivot):
            p = k
            for i in range(k+1, n):
                if(abs(A[i][k]) > abs(A[p][k])):
                    p = i
            if(p != k):
                A[k], A[p] = A[p], A[k]
                B[k], B[p] = B[p], B[k]

        for i in range(k+1, n):
            temp = A[i][k]/A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - temp*A[k][j]

            B[i] = B[i] - temp*B[k]
        
        if(showall):
            print(f"A/step-{step}: {A}")
            print(f"B/step-{step}: {B}")
        step += 1

    # back substitution
    roots[n-1] = round(B[n-1]/A[n-1][n-1], 4)
    for i in range(n-2, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += A[i][j]*roots[j]
        xi = (B[i] - s)/A[i][i]
        roots[i] = round(xi, 4)

    return roots


A = []
A.insert(0, [sum('x^2', N), sum('x', N)])
A.insert(1, [sum('x', N), sum('1', N)])

B = []
B.insert(0, sum('xy', N))
B.insert(1, sum('y', N))

result = GaussianElimination(A, B, False, False)
a = exp(result[1])
b = result[0]

print(f'a = {a}, b = {b}')

file.close()