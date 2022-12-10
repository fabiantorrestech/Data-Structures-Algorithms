# problem: https://leetcode.com/problems/remove-duplicate-letters/ or https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# - TIME: O(n)
# - SPACE: O(3n) -> O(n)

from collections import deque

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        lookup = dict()         # store the latest seen index for each character in 's'
        for i in range(len(s)):
            lookup[s[i]] = i
        
        stack = deque()         # will use to construct the string
        seen = set()            # will use to determine if we have seen a character yet.
        for i in range(len(s)):
            if s[i] in seen: continue       # if we have aleady seen, just skip this char.
                
            while (stack and                # while stack is not-empty AND
                   stack[-1] > s[i] and     #       stack-top char > s[i] AND  -- (ex: c @ stack-top > 'a' in s[i])
                   lookup[stack[-1]] > i):  #       stack-top char occurs later than curr-index
                
                seen.remove(stack[-1])      # remove stack-top char from 'seen' set.
                stack.pop()                 # remove stack-top char from stack!
            
            stack.append(s[i])              # add s[i] to stack
            seen.add(s[i])                  # add s[i] to 'seen' set.
        
        return ''.join(stack)               # the final stack will be the answer.