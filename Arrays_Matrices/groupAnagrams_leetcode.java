// problem: https://leetcode.com/problems/group-anagrams/
// TIME: O(n) 
// SPACE: O(n)
// - optimal solution implemented in java. Utilize a Hashmap with <k,v> = <sorted_s, [anagram1FromStrs, anagram2FromStrs]>

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List<String>> answer = new HashMap<>();

        for(String s : strs){
            // sort the word first
            char[] s_array = s.toCharArray();
            Arrays.sort(s_array);
            String s_sorted = new String(s_array);

            // add the sorted word as a key in our 'answer' hashmap intially with an empty List value.
            if(!answer.containsKey(s_sorted))
                answer.put(s_sorted, new ArrayList<>());

            // add the string into the list values.
            answer.get(s_sorted).add(s);
        }

        return new ArrayList<>(answer.values());
    }
}