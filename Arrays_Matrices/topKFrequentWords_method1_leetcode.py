# problem: https://leetcode.com/problems/top-k-frequent-words/submissions/
# - TIME: O(n*logn). If words is all distinct elements, then it will be O(nlogn). if it is not the case, then it is O(n*logk) on average.
# - SPACE: O(n*log)

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        wordCount = Counter(words)                                 # count frequency of each string in 'words' list.
        
        heap = [(-freq, word) for word, freq in wordCount.items()] # create heap: list of tuples() -> [(frequency, word), ...]
                                                                   # - by default, python makes a min-heap. We want a max heap.
                                                                   #   So constructing a min-heap with negative values will give us a max heap! (:
        heapq.heapify(heap)
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans
        
        
        
        