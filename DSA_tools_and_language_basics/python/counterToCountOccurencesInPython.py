from collections import Counter

givenList = ["a", "a", "a", "a", "a", "b", "b", "x", "y", "z", "z"]

count = Counter(givenList)
print(count)

# convery Counter-dict to regular dict
regularDict = dict(count)
print(regularDict)

# dictionary with reversed k,v
dictWithReversedKV = dict((v,k) for k,v in count.items())
print(dictWithReversedKV)