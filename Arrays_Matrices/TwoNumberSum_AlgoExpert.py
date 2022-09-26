def twoNumberSum(array, targetSum):
    seenNumbers={}
    
    for x in array:
        y = targetSum-x
        numExistsInDict = seenNumbers.get(y)
        if numExistsInDict:
            return [x,y]
        seenNumbers[x] = True
    return []

# time: O(n)
# space: O(n)
#
# 1) x + y = targetSum
# 2) y = targetSum - x
