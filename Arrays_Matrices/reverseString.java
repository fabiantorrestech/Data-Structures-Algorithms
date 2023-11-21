// problem: https://leetcode.com/problems/reverse-string/
// TIME: O(logn)
// Space O(1)
//
// - its important to note that you can only do this with a char array. So in order to do with a String, you need to convert the string to a char-array.
// - YOU CANNOT DO THIS WITH A built-in 'String' object!!
// - *** This is doing it without StringBuilder or StringBuffer.

class Solution {
    public void reverseString(char[] s) {
        
        int left = 0;
        int right = s.length-1;
        char temp = ' ';
        while(left < right){
            temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
        
    }
}