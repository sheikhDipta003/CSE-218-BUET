def f(*args):
    tpl = args[0]
    print("{", tpl)
    # n = len(args)
    if(not isinstance(tpl, float)):
        n = len(tpl)
    else:
        n = 1

    if(n == 1):
        if(isinstance(tpl, float)):
            print("1. ",args)
            return Gene_exp[Time.index(tpl)]
        else:
            print("2. ",args)
            return Gene_exp[Time.index(tpl[0])]
    return (f(args[1:n+1]) - f(args[0:n-1]))/(args[n-1] - args[0])

def f1(T):
    n = len(Time)
    diff = []
    points = []
    for i in range(0, n):
        if(Time[i] >= T):
            c = '+'
        else:
            c = '-'
        diff.append((abs(Time[i]-T), c))
    
    diff.sort()

    for i in range(0, 4):
        if(diff[i][1]== '+'):
            points.append(diff[i][0] + T)
        else:
            points.append(T - diff[i][0])
    
    points.sort()
    # print(points)
    # print(f(points[0], points[1], points[2]))

    b = []
    b.insert(0, f(points[0]))
    b.insert(1, f(points[0], points[1]))
    b.insert(2, f(points[0], points[1], points[2]))
    b.insert(3, f(points[0], points[1], points[2], points[3]))
    # print(b)
    return b[0] + b[1]*(T - points[0]) + b[2]*(T - points[0])*(T - points[1]) + b[3]*(T - points[0])*(T - points[1])*(T - points[2])


Time = []
Gene_exp = []
with open("gene.txt") as file:
    lines = [line.strip() for line in file]
    Time = [float(t.split()[0]) for t in lines]
    Gene_exp = [float(t.split()[1]) for t in lines]
    # print(Time, Gene_exp)

result = f1(16)
print(result)
file.close()