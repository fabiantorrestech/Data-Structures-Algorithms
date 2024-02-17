// problem: https://leetcode.com/problems/decode-the-message/
// TIME:
// SPACE: 


class Solution {
  public String decodeMessage(String key, String message) {

      // remove the spaces and non-unique letters from key.
      Set<Character> seenChars = new HashSet<>();
      String newKey = "";
      for(int i=0; i<key.length(); i++){
          Character c = key.charAt(i);
          if(c == ' ' || seenChars.contains(c))
              continue;
          newKey+=Character.toString(c);
          seenChars.add(c);
      }

      // populate the decode table (a-z). <k,v> -> <keyChar, alphaChar>
      Map<Character, Character> decodeTable = new TreeMap<>();
      decodeTable.put(' ', ' ');
      char alphaChar = 'a';
      for(int i=0; i<newKey.length(); i++){
          char keyChar = newKey.charAt(i);
          if(decodeTable.containsKey(keyChar))
              continue;
          decodeTable.put(keyChar, alphaChar);
          alphaChar++;
      }

      // now decode the message. Store it in 'ans'.
      String ans = "";
      for(Character ch : message.toCharArray())
          ans += decodeTable.get(ch);

      return ans;        
  }
}