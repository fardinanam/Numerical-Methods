def gaussianElimination(A, B):
    rows = len(A)
    columns = len(A[0])
    step = 0

    for i in range(rows - 1):  # Forward elimination
        j = i + 1

        if A[i][i] == 0:
            for z in range(j, rows):
                if A[z][i] != 0:
                    t = i
                    while t < columns:
                        temp = A[i][t]
                        A[i][t] = A[z][t]
                        A[z][t] = temp
                        t = t + 1
                    temp = B[i][0]
                    B[i][0] = B[z][0]
                    B[z][0] = temp
                    break

        while j < rows:
            factor = A[j][i] / A[i][i]
            k = i
            while k < columns:
                A[j][k] = A[j][k] - factor * A[i][k]
                k = k + 1
            B[j][0] = B[j][0] - factor * B[i][0]
            j = j + 1
        
    X = []

    for x in range(rows):
        X.append(0)
    i = rows - 1

    for i in range(rows - 1, -1, -1):  # Back substitution
        sum = 0
        j = columns - 1
        while j > i:
            sum = sum+A[i][j] * X[j]
            j = j - 1
        X[j] = (B[j][0] - sum) / A[i][i]

    return X