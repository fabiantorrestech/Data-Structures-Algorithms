def calcPermutation(self, n, r) -> int:
    nFact = math.factorial(n)
    nMinusRFact = math.factorial(n-r)
    nPr = nFact // nMinusRFact
    return nPr