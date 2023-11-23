// problem: 
// TIME: O(n*logn)
// SPACE: O(n)
// - This method is less efficient because we need to sort both charArrays. That takes n*logn time for each array.


class Solution {
    
    public boolean isAnagram(String s, String t) {
        char sCharArray[] = s.toCharArray();
        char tCharArray[] = t.toCharArray();
        Arrays.sort(sCharArray); // sort using built-in Arrays.sort()
        Arrays.sort(tCharArray);
        
        return Arrays.equals(sCharArray, tCharArray); // compare the 2 using built-in Arrays.equals()
    }
}