def calculateFactorial(self, x) -> int:
    if x == 0:  # base case: 0! = 1
        return 1
    
    xFact = 1
    for i in range(1, x+1):
        print(i)
        xFact = xFact * i
    return xFact