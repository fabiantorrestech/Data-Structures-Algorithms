def twoNumberSum(array, targetSum):
    answerArr = []

    for i in array:
        for j in array:
            if not i == j and i+j == targetSum:
                if i in answerArr and j in answerArr:
                    pass
                elif i in answerArr and not j in answerArr:
                    answerArr.append(j)
                elif j in answerArr and not i in answerArr:
                    answerArr.append(i)
                else:
                    answerArr.append(i)
                    answerArr.append(j)
    return answerArr

# ~~~ Easy
# time -- O(n^2)
# space -- O(n) 