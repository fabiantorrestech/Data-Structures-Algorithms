// problem: 
// TIME: O(n)
// SPACE: O(n)
// - Time is O(n) because we need to loop through each input-string once to populate the new hashmaps. 
// - And space is O(n) because we need to populate hashmaps of equivalent size as input strings.

class Solution {
    public void printHM(HashMap<Character, Integer> hm){
        for(Character c : hm.keySet()){
            System.out.println(c + " = "+ hm.get(c));
        }
    }
    
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> charCountS = new HashMap<Character, Integer>();
        HashMap<Character, Integer> charCountT = new HashMap<Character, Integer>();
        
        // populate the S hashmap (to count all characters in s)
        for(int i = 0; i<s.length(); i++){
            if(!charCountS.containsKey(s.charAt(i))){
                charCountS.put(s.charAt(i), 1);
            }
            else{
                charCountS.put(s.charAt(i), charCountS.get(s.charAt(i)) + 1);
            }
        }
        
        // populate the T hashmap (to count all characters in t)
        for(int i = 0; i<t.length(); i++){
            if(!charCountT.containsKey(t.charAt(i))){
                charCountT.put(t.charAt(i), 1);
            }
            else{
                charCountT.put(t.charAt(i), charCountT.get(t.charAt(i)) + 1);
            }
        }

        // check if both the hashmaps have the same number of characters.
        if(charCountS.equals(charCountT)){
            return true;
        }
        
        return false;
    }
}