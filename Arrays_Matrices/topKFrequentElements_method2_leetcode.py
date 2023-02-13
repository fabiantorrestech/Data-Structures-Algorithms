# problem:  https://leetcode.com/problems/top-k-frequent-elements/submissions/
#
# - TIME: O(n*logk) 
#
#        - takes O(n) time to build hashmap. 
#
#        - BUILDING THE HEAP:
#          Time for inserting into k-sized heap: O(logk), for k elements. 
#          Popping least freq element from k-sized heap: O(logk). This is done 'n-k' times.
#          ... So overall, building the heap takes O(n-k*logk) --> O(nlogk) time.
#
#        - O(k) time to pick the top k elements since O(1) for taking all elements from k-sized heap.
#         
# - SPACE: O(n+k) - hashmap is O(n), heap is of size k so O(k).
#
#   - slightly less optimal solution but much more inutive to code instead of bucketSort.


from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        charCount = Counter(nums)   # dict = <k,v> -> <elem, frequency>
        
        return heapq.nlargest(k, charCount.keys(), key=charCount.get) # .nlargest() asks for 
                                                                        # - k = number of elements
                                                                        # - iterable = what to pick the elements from
                                                                        # - key = based on what? (in this case, frequency)
        
        