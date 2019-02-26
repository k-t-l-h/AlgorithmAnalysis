def standart_matrix_mult(a, b):
    m = len(a)
    n = len(a[0])
    q = len(b[0])
    c = [[0 for x in range(q)] for y in range(m)]

    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k]*b[k][j]
    return c


def classic_vinograd_mult(a, b):
    m = len(a)
    n = len(a[0])
    q = len(b[0])
    c = [[0 for x in range(q)] for y in range(m)]
    t = n//2+1

    row_fact = [0 for x in range(m)]
    column_fact = [0 for x in range(q)]


    for i in range(m):
        row_fact[i] = 0
        for j in range(1, t):
            row_fact[i] = row_fact[i] + a[i][2*j-2] * a[i][2*j-1]

    for i in range(q):
        column_fact[i] = 0
        for j in range(1, t):
            column_fact[i] = column_fact[i] + b[2*j-2][i] * b[2*j-1][i]

    for i in range(m):
        for j in range(q):
            c[i][j] = -row_fact[i] - column_fact[j]
            for k in range(1, t):
                c[i][j] = c[i][j] + (a[i][2*k-2]+b[2*k-1][j])*(a[i][2*k-1] + b[2*k-2][j])

    if (n % 2 == 1):
        for i in range(m):
            for j in range(q):
                c[i][j] = c[i][j] + a[i][n-1]*b[n-1][j]

    return c

def optimized_vinograd_mult(a, b):
    m = len(a)
    n = len(a[0])
    q = len(b[0])
    c = [[0 for x in range(q)] for y in range(m)]
    t = n-1

    row_fact = [0 for x in range(m)]
    column_fact = [0 for x in range(q)]


    for i in range(m):
        for j in range(0,t,2):
            row_fact[i] += a[i][j] * a[i][j+1]

    for i in range(q):
        for j in range(0,t,2):
            column_fact[i] += b[j][i] * b[j+1][i]

    for i in range(m):
        for j in range(q):
            c[i][j] = -row_fact[i] - column_fact[j]
            for k in range(0,t,2):
                c[i][j] += (a[i][k]+b[k+1][j])*(a[i][k+1] + b[k][j])

    if (n % 2):
        for i in range(m):
            for j in range(q):
                c[i][j] += a[i][n-1]*b[n-1][j]

    return c
