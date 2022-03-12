import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import pandas as pd

def f(x):
    if(x == 1 or x<=-2):
        print("Input out of domain")
        sys.exit()
    return (x / (1-x))*(math.sqrt(6 / (2 + x))) - 0.05

def fAll(x):
    y = []
    for t in x:
        y.append(f(t))
    return y

def error(xOld, xNew):
    return abs((xNew-xOld)/xNew) * 100

def findRootByBisection(xl, xu, Es, iterations):
    yl = f(xl)
    yu = f(xu)
    
    if(yl == 0):
        return xl
    elif(yu == 0):
        return xu
    elif(yl * yu > 0):
        print(f"No roots can be found between ({yl},{yu})")
        sys.exit()
    
    for i in range(0, iterations):
        xm = (xl + xu) / 2
        ym = f(xm)

        if(ym == 0):
            return xm
        elif(yl * ym < 0):
            xu = xm
        else:
            xl = xm
            
        if(i != 0 and error(xOld, xm) <= Es):
            return xm

        xOld = xm
        
    return "No root found (Maximum iterations reached)"
    
def table(xl, xu, Es):
    yl = f(xl)
    yu = f(xu)
    errors = []
    
    if(yl == 0):
        return xl
    elif(yu == 0):
        return xu
    elif(yl * yu > 0):
        print(f"No roots can be found between ({yl},{yu})")
        sys.exit()
    
    for i in range(0, 21):
        print(f"i = {i}")
        xm = (xl + xu) / 2
        ym = f(xm)

        # if(ym == 0):
        #     return xm
        if(yl * ym < 0):
            xu = xm
        else:
            xl = xm
        
        if(i != 0):
            errors.append(error(xOld, xm))
        xOld = xm

    s = pd.Series(errors, index=range(1, 21))
    data = pd.DataFrame({'Absolute Relative Approx. Errors': s})
    print(data)


if __name__ == "__main__":
    print(f"The root of the function is {findRootByBisection(-1, .9, 0.05, 10000)}")
    table(-1, 0.9, 0.05)

    fig, ax = plt.subplots()

    t1 = np.arange(-1.9,1, 0.1)
    t2 = np.arange(1.1,5,0.1)

    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    plt.plot(t1,fAll(t1))
    plt.plot(t2, fAll(t2))
    plt.show()