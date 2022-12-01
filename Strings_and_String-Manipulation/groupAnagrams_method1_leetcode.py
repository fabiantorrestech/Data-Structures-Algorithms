# problem: https://leetcode.com/problems/group-anagrams/
# - TIME: O(m*n), where m is number of words in 'strs', n is the avg length of each string in 'strs'
# - SPACE: O(m(26*n)) -> O(m*n) ...because our hashmap (of size 26) for each str will traverse the entire length of
#                                  each string in strs (n). and we must do this 'm' times for each string in 'strs'. 
#   - Optimal solution. Very Pythonic.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)                  # defaultdict is same as dict, but instead doesn't give key errors when key DNE. 
                                                    # <k,v> -> k = list[]
            
        for currStr in strs:
            count = [0] * 26                       # occurences of all lowercase characters (a-z)
            
            for currChar in currStr:
                count[ord(currChar)-ord('a')] += 1 # count occurence of currStr[currChar] in hashmap/array (count).

            key = tuple(count)                     # lists/arrays cannot be keys in a dictionary, so convert it tuple().
                                                   #    - tuples() are immutable. so only immutable objects can be keys for dict().

            result[key].append(currStr)            # use the tuple(count[]) as the key. so all other strings that have the same tuple(count[]), will append currStr as a value as well.

        return result.values()                     # <k,v> = <tuple(), [str1, str2, str3...]>
                                                   #    - so if we return only the values, will be returned in list of values
                                                   #    - values: [[str1,str2, str3], [str5], [str4, str6]]

        

# ex: ["eat","tea","tan","ate","nat","bat"]
#
# - defaultdict(<class 'list'>, 
#   {
#     (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'],
#     (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'],
#     (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']
#   })






        
        