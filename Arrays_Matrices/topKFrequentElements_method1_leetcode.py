# problem: https://leetcode.com/problems/top-k-frequent-elements/
# - TIME: O(n)
# - SPACE: O(n)
#   - Most optimal solution for this particular problem: Bucket-Sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        charCount = dict()
        freq = [[] for i in range(len(nums)+1)]
        ans = []
        
        for i in range(len(nums)):      # obtain number of occurences of each element in nums
            charCount[nums[i]] = 1 + charCount.get(nums[i], 0)
        
        for key, val in charCount.items():  # loop through dictionary to populate freq Array
                                            # populated freq array accordingly: i=number of times occured, freq[i] = elements that have occurred 'i' number of times 
            freq[val].append(key)
        
        for i in range(len(freq)-1, 0, -1): # go through each 'bucket' in freq starting from end (top occuring elements)
            for n in freq[i]:               # look through the sub-bucket, and handpick only k elements for answer array.
                if len(ans) == k:
                    return ans
                ans.append(n)
            
        return ans
        
        