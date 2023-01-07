
s1 = "abd"
chars = [0] * 26                        # list of 26 letters.
for i in range(len(s1)):
    chars[ord(s1[i]) - ord('a')] +=1    # increment idx in chars[] corresponding to letter at s1[i]
                                        # a = chars[0], b = chars[1], c = chars[2]... z = chars[25]
                                        # 1             1             0               0

                                        # ord() -> returns ascii value of parameter.

print(chars)