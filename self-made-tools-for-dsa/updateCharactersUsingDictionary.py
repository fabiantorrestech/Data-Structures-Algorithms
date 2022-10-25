
# - will only update given 'chars' dict for 1 occurence of a char at s[i].
# - to count all chars, call method in a loop.
def updateCharDict(s: str, i: int, chars: 'dict[str, int]', remove: bool) -> None:
    if remove == True:
        if char.get(s[i]) == 1:
            chars[s[i]] = 0  # set char count to 0 in dict.
        else:
            char[s[i]] -= 1   # decrement char-count in dict
    else:
        if not s[i] in chars: # add char to dictionary
            chars[s[i]] = 1
        else:                 # count occurence to dict
            chars[s[i]] += 1
    

# --- EXAMPLE USAGE ---
myStr = "hamster"
myDict = {}

for i in range(len(myStr)):
    updateCharDict(myStr, i , myDict, False)

print(myDict)
        