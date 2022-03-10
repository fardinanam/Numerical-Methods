import math

g = 9.8

def f(t : float) -> float:
    u = 2000
    q = 2100
    mo = 140000
    valueToBeLogged = mo / (mo - q * t)

    return u * math.log(valueToBeLogged) - g * t

def areaOfTrapezoid(start : float, end : float) -> float:
    return (end - start) * ((f(start) + f(end)) / 2)


def integrationWithTrapezoidalRule(start: float, end: float, subIntervals: int) -> float :
    lengthOfAnInterval = (end - start) / subIntervals
    sumOfArea = 0

    for i in range(0, subIntervals):
        newStart = start + i * lengthOfAnInterval
        newEnd = newStart + lengthOfAnInterval

        sumOfArea += areaOfTrapezoid(newStart, newEnd)
    
    return sumOfArea


def simpsonsRule(start: float, end: float) -> float :
    h = (end - start) / 2
    fStart = f(start)
    fEnd = f(end)
    fHalf = f((start + end) / 2)

    return (h / 3) * (fStart + 4 * fHalf + fEnd)

def integrationWithSimpsonsRule(start: float, end: float, subIntervals: int) -> float:
    lengthOfAnInterval = (end - start) / subIntervals
    integratedValue = 0

    for i in range(0, subIntervals):
        newStart = start + i * lengthOfAnInterval
        newEnd = newStart + lengthOfAnInterval

        integratedValue += simpsonsRule(newStart, newEnd)
    
    return integratedValue

def error(oldValue, newValue):
    return (abs(oldValue - newValue) / newValue) * 100

if __name__ == "__main__":
    start = 8
    end = 30
    print("Number of sub-intervals: ")
    n = int(input())

    valueOfTR = integrationWithTrapezoidalRule(start, end, n)
    valueOfSR = integrationWithSimpsonsRule(start, end, n)

    print(f"Calculated value of distance using trapizoidal rule is {valueOfTR} meters")
    print(f"Calculated value of distance using Simpson's 1/3rd rule is {valueOfSR} meters")

    oldValueOfTR = 0
    oldValueOfSR = 0

    print()
    print("Trapezoidal Rule: ")
    print("n\tValue of integral\tAbsolute approximate relative error")
    for i in range(1, 6):
        valueOfTR = integrationWithTrapezoidalRule(start, end, i)
        
        absoluteRelativeErrorForTR = "---"

        if(i != 1):
            absoluteRelativeErrorForTR = error(oldValueOfTR, valueOfTR)            

        print(f"{i}\t{valueOfTR}\t{absoluteRelativeErrorForTR}")
        
        oldValueOfTR = valueOfTR
        
    print()
    print("Simpson's 1/3rd rule: ")
    print("n\tValue of integral\tAbsolute approximate relative error")
    for i in range(1, 6):
        valueOfSR = integrationWithSimpsonsRule(start, end, i)
        
        absoluteRelativeErrorForSR = "---"

        if(i != 1):
            absoluteRelativeErrorForSR = error(oldValueOfSR, valueOfSR)            
        
        print(f"{i * 2}\t{valueOfSR}\t{absoluteRelativeErrorForSR}")
        
        oldValueOfSR = valueOfSR