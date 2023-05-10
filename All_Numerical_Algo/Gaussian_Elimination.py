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


n = int(input())
print()

lhs = []
for i in range(0, n):
    lhs.insert(i, [float(a) for a in input().split()])
print()

rhs = []
for i in range(0, n):
    rhs.insert(i, float(input()))
print()

soln = GaussianElimination(lhs, rhs)
for x in soln:
    print(x)

# -2 0 1
# -1 7 1
# 5 -1 1
# -4
# -50
# -26
# soln: [-4 -6 -12]