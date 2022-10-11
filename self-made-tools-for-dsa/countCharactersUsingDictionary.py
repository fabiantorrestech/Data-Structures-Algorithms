import string

# given str, returns dict() with occurences of each letters
# - <k,v> => <char, numOfOccurences>
def countChars(s: string):
    seenChars = dict()

    for char in s:
        if char in seenChars:
            seenChars[char] += 1
        else:
            seenChars[char] = 1

    return seenChars





myStr = "hello"
characterOccurences = countChars(myStr)
print(characterOccurences)
