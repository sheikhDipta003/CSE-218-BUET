import matplotlib.pyplot as plt

def f(x):
    return -(6.73 * x + 6.725 * pow(10, -8) + 7.26 * pow(10, -4) * 5 * pow(10, -4))/(3.62 * pow(10, -12) * x + 3.908 * pow(10, -8) * 5 * pow(10, -4) * x)

def sum(a, h, n1, n2):
    sum = 0
    for i in range(n1, n2):
        sum += f(a + i * h)
    return sum

def I_t(a, b, n):
    h = (b - a) / n
    return h * 0.5 * (f(a) + 2 * sum(a, h, 1, n) + f(b))

def I_s_2(a, b):
    h = (b - a) / 2
    return (h/3) * (f(a) + 4 * f((a + b) / 2) + f(b))

def I_s(a, b, n):
    I = 0
    h = (b - a) / (2 * n)
    for k in range(0, 2*n, 2):
        I += I_s_2(a + k * h, a + (k+2) * h)
    return I

def error(a, b, n, ch):
    if(n <= 1):
        return None
    if(ch=='t'):
        prev = I_t(a, b, n-1)
        curr = I_t(a, b, n)
    elif (ch=='s'):
        prev = I_s(a, b, n-1)
        curr = I_s(a, b, n)
    return abs((curr - prev) / curr) * 100

def show(x1, x2, n1, n2, ch):
    print("\nResult\t\t\tAbsolute Relative Approximate Error")
    for i in range(n1, n2+1):
        if(ch=='t'):
            print(f"{I_t(x1, x2, i)}\t{error(x1, x2, i, 't')}")
        elif(ch == 's'):
            print(f"{I_s(x1, x2, i)}\t{error(x1, x2, i, 's')}")

show(1.22 * pow(10, -4), 0.61 * pow(10, -4), 1, 5, 't')
show(1.22 * pow(10, -4), 0.61 * pow(10, -4), 1, 5, 's')

# plotting
x = [1.22 * pow(10, -4), 1.20 * pow(10, -4), 1.0 * pow(10, -4), 0.8 * pow(10, -4), 0.6 * pow(10, -4), 0.4 * pow(10, -4), 0.2 * pow(10, -4)]
t = [I_s(1.22 * pow(10, -4), b, 5) for b in x]

fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(6)
plt.plot(t, x)
plt.axis([0, 3 * pow(10, 7), 0, 1.4 * pow(10, -4)])
plt.title('Concentration of Remaining Oxygen in Fuel Cell with Time')
plt.xlabel('time(s)')
plt.ylabel('concentration(mole/cc)')
plt.grid()
plt.show()
