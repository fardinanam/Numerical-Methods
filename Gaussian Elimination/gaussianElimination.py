import numpy as np

def gaussianElimination(A, B, d):
    matrix = np.append(A, B, axis=1)
    n = B.size

    # Every row except the first one have to change. So, rows - 1 steps
    for i in range(n - 1):
        # Every step has totalRows - currentStep number of sub steps
        for j in range(i + 1, n):
            matrix[j] = matrix[j] - matrix[i] * (matrix[j, i] / matrix[i, i])

            if d:
                print(f"\nStep {i + 1},{j - i}")
                A = matrix[:, : n]
                B = matrix[:, n:]
                print("Matrix of A:\n", A)
                print("Matrix of B:\n", B)

    x = np.zeros(n, dtype=float)
    # x[n - 1] = B[n - 1]/A[n - 1, n - 1]

    for i in range(n - 1, -1, -1):
        x[i] += B[i]

        for j in range(i + 1, n):
            x[i] -= A[i, j] * x[j]

        x[i] /= A[i, i]

    print("\nCalculated Solutions of X:")
    for i in range(n):
        print("%.4f" % (x[i]))


if __name__ == "__main__":
    n = int(input())
    A = []

    for i in range(n):
        a = []
        for j in range(n):
            a.append(float(input()))
        A.append(a)

    A = np.array(A)
    b = []
    for i in range(n):
        b.append([float(input())])

    B = np.array(b)
    gaussianElimination(A, B, True)