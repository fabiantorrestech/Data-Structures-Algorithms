from collections import Counter

# Counter objects are a variation of dict(). Where <k,v> = <k, numOfOccurencesInDataStructure>

# 1: for counting number of repeated strings in a list *** MOST COMMON USE CASE ***
# - sorted based on frequency (greatest -> lowest)
words = ["i","love","leetcode","i","love","coding"]
count1 = Counter(words)
print(f"count1 from a list: {count1}")

# 2: for counting with an input of dictionary       *** 2nd MOST COMMON USE CASE ***
# - sorted based on frequency (greatest -> lowest)
myDict = {"A": 3, "B": 5, "C": 2}
count2 = Counter(myDict)
print(f"count2 from a dictionary: {count2}")

#3: for counting with inputs as keywords
count3 = Counter(A=3, B=5, C=2)
print(f"count3 with keywords: {count3}")