// problem: https://leetcode.com/problems/first-unique-character-in-a-string/
// - TIME: O(2n) -> O(n)
// - SPACE: O(1)
// - most optimal solution, except utilizing an array for counting characters.

class Solution {
  public int firstUniqChar(String s) {
      // utilize a 26 size array to keep character count.
      int[] charCount = new int[26];
      for(int i=0; i<s.length(); i++){
          char c = s.charAt(i);
          charCount[c-'a']++;
      }
      
      // loop through string one more time to find character with count=1, then return it
      for(int i=0; i<s.length(); i++){
          char c = s.charAt(i);
          if(charCount[c-'a']==1)
              return i;
      }
      
      return -1;
  }
}