import gaussianElimination as ge
import numpy as np
import matplotlib.pyplot as plt

def readFromFile():
    f = open("input.txt", "r")
    readLine = f.readlines()[1:]

    xs = []
    ys = []

    for line in readLine:
        xs.append(float(line.split()[0]))
        ys.append(float(line.split()[1]))
    
    f.close()

    return xs, ys

def regressionValuesY(xs, coefficients):
    n = len(xs)
    order = len(coefficients) - 1

    yValueAfterRegression = []

    for i in range(n):
        y = coefficients[0]

        for j in range(1, order + 1):
            y = y + coefficients[j] * (xs[i] ** j)
        
        yValueAfterRegression.append(y)

    return yValueAfterRegression

def polynomialRegression(xs : list, ys : list, order : int):
    n = len(xs)
    A = np.zeros((order + 1, order + 1))
    B = np.zeros((order + 1, 1))

    for i in range(order + 1):
        for j in range(i + 1):
            k = i + j
            sum = 0

            for l in range(n):
                sum = sum + xs[l] ** k
            
            A[i, j] = sum
            A[j, i] = sum
        
        sum = 0

        for l in range(n):
            sum = sum + ys[l] * (xs[l] ** i)
        
        B[i, 0] = sum

    # print(A)
    # print(B)
    coefficients = ge.gaussianElimination(A, B)
    yValues = regressionValuesY(xs, coefficients)

    return coefficients, yValues

def exponentialRegression(xs: list, ys: list):
    lnYs = np.log(ys)
    
    coefficients, zValues = polynomialRegression(xs, lnYs, 1)
    coefficients[0] = np.exp(coefficients[0])

    yValues = np.exp(zValues)

    return coefficients, yValues

def graph(xs : list, ys : list, regressionYs : list):
    fig, ax = plt.subplots()
    ax.scatter(xs, ys, color = 'green', label = 'Given points')
    
    ax.plot(xs, regressionYs, label='Regression line')

    ax.legend()
    plt.show()

if __name__ == "__main__":
    xs, ys = readFromFile()
    # coefficients, yValues = polynomialRegression(xs, ys, order = 2)
    coefficients, yValues = exponentialRegression(xs, ys)

    print(f"Coefficients: {coefficients}")
    graph(xs, ys, yValues)
