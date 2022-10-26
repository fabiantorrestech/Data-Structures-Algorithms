# given str, returns dict() with occurences of each letters
# - <k,v> => <char, numOfOccurences>
# - counts all chars in string with 1 call!
def countChars(s: str):
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
