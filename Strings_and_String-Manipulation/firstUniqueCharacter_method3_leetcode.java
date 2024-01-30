// problem: https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution {
  public int firstUniqChar(String s) {
      
      // create a hashmap with the last seen index of each character
      char[] sChars = s.toCharArray();
      Map<Character, Integer> uniqueIdx = new HashMap<>();
      Set<Character> seen = new HashSet<>();
      for(int i=0; i<sChars.length; i++){
          char c = sChars[i];
          if(!uniqueIdx.containsKey(c) && !seen.contains(c)){
              uniqueIdx.put(c, i);
              seen.add(c);
          }
          else
              uniqueIdx.remove(c);
      }
      
      if(uniqueIdx.size() < 1)
          return -1;
      
      // now pick the key from hashmap with smallest value
      int ans = Integer.MAX_VALUE;
      for(Character c : uniqueIdx.keySet()){
          if(uniqueIdx.get(c) < ans)
              ans = uniqueIdx.get(c);
      }
      
      return ans;
  }
}