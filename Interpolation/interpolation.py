import numpy as np

def lagrageFunction(i, xs, x):
    Li = 1
    n = xs.shape[0]

    for j in range(0, n):
        if j != i:
            Li *= (x - xs[j]) / (xs[i] - xs[j])
    
    return Li


def lagragesInterpolation(xs, ys, x):
    n = xs.shape[0]
    y = 0

    for i in range(0, n):
        y += lagrageFunction(i, xs, x) * ys[i]

    return y

def newtonsDividedDifferenceCoefficient(xs, ys):
    n = xs.shape[0]

    if xs.shape[0] == 1:
        return ys[0]
    
    return (newtonsDividedDifferenceCoefficient(xs[1 : ], ys[1 : ]) - newtonsDividedDifferenceCoefficient(xs[ : n - 1], ys[ : n - 1])) / (xs[n - 1] - xs[0])

def newtonsDividedDifference(xs, ys, x):
    n = xs.shape[0]
    y = 0

    for i in range(0, n):
        b = newtonsDividedDifferenceCoefficient(xs[ : i + 1], ys[ : i + 1])

        for j in range(0, i):
            b *= (x - xs[j])
        
        y += b
    
    return y


if __name__ == "__main__":
    x = [10, 15, 20, 22.5]
    y = [227.04, 362.78, 517.35, 602.97]

    xs = np.array(x)
    ys = np.array(y)

    # print(lagragesInterpolation(xs, ys, 16))
    print(newtonsDividedDifference(xs, ys, 16))