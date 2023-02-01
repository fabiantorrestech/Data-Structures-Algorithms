# problem: https://leetcode.com/problems/fizz-buzz/submissions/
# - TIME: O(n)
# - SPACE: O(1)
#   - non-modulo answer (since modulo operation is costly/slow...)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        # range(start, stop, step)
        # - start: (inclusive) since list-indices are still 0 indexed, must start at number=idx-1 for range.
        # - stop: non-inclusive
        # - step: how much to add to 'start' and that will be the next i.
        
        output = [str(x) for x in range(1, n+1)]            # creating a list with string-converted integers from [1,n]
        
        for i in range(2, n, 3):
            output[i]="Fizz"
        
        for i in range(4, n, 5):
            output[i]="Buzz"
        
        for i in range(14, n, 15):
            output[i]="FizzBuzz"
        
        return output