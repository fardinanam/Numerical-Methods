import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 3 - 0.165 * (x ** 2) + 3.991e-4

def df(x):
    return 3 * (x ** 2) - 0.33 * x

def error(xOld, xNew):
    return abs((xOld - xNew) / xNew) * 100

def numberSignificantDigitsCorrect(error):
    if error > 5:
        return 0
    elif error <= 5 and error >= 1:
        return 1
    else:
        n = 0
        while error < 5:
            error *= 10
            n += 1
        
        return n


def findRootByNewtonRaphsonMethod(initialGuessX, relativeErrorTolerance, maxNumberOfIteration):
    xOld = initialGuessX
    
    for i in range(0, maxNumberOfIteration):
        xNew = xOld - f(xOld) / df(xOld)
        relError = error(xOld, xNew)

        print(f"Number of correct digits {numberSignificantDigitsCorrect(relError)}")

        if relError <= relativeErrorTolerance:
            return xNew

        xOld = xNew

    return "No root found. Max number of iterations reached."

print(findRootByNewtonRaphsonMethod(0.05, 0.05, 3))

x = np.arange(0, 0.1, 0.005)
y = f(x)

fig, ax = plt.subplots()

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

plt.plot(x, y)
plt.show()
