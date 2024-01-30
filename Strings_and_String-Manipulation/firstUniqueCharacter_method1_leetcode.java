// problem: https://leetcode.com/problems/first-unique-character-in-a-string/
// - TIME: O(2n) -> O(n)
// - SPACE: O(n)
// - most optimal solution, except utilizing a hashmap.

class Solution {
  public int firstUniqChar(String s) {
      
      // utilize hashmap to keep count of characters
      Map<Character, Integer> charCount = new HashMap<>();
      for(int i=0; i<s.length(); i++){
          char c = s.charAt(i);
          if(charCount.containsKey(c))
              charCount.put(c, charCount.get(c)+1);
          else
              charCount.put(c, 1);
      }
      
      // now go through original string 1 more time, but if current character's count in hashmap is 1, then return that character.
      for(int i=0; i<s.length(); i++){
          char c = s.charAt(i);
          if(charCount.get(c)==1)
              return i;
      }
      
      return -1;
  }
}