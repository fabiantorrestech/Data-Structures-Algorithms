// problem: https://leetcode.com/problems/rotate-array/
// - TIME: O(n)
// - SPACE: O(1)
//      - optimal solution if you cant use Collections library.

import java.util.Arrays;
import java.util.Collections;

class Solution {
    
    public void rotate(int[] nums, int k) {
        
        // if k > nums.length, it is unncessary work to rotate array more than k times.  
        if(k > nums.length){ k = k%nums.length;}    
        
        // convert Java int[] -> Integer[] -- creating another Integer Array[nums.length]
        Integer integerNums[] = new Integer[nums.length];
        for(int i=0; i<nums.length;i++){
            integerNums[i] = Integer.valueOf(nums[i]);
        }
        
        Collections.reverse(Arrays.asList(integerNums));  // reverse the entire array once
        
        
        // reverse only the first [0,k-1] elements
        Integer[] firstKArr = Arrays.copyOfRange(integerNums, 0, k);    // reverses from [startIdx, endIdx)
        Collections.reverse(Arrays.asList(firstKArr));
        
        Integer[] lastKtoNArr = Arrays.copyOfRange(integerNums, k, integerNums.length); // now reverse the last [k, n] elements
        Collections.reverse(Arrays.asList(lastKtoNArr));
        
        
        // now concatenate the two halves of the arrays together
        Integer[] answer = new Integer[nums.length];
        System.arraycopy(firstKArr, 0, answer, 0, k);
        System.arraycopy(lastKtoNArr, 0, answer, k, nums.length-k);
        
        // convert Integer back to int type array and return that
        for(int i=0; i<nums.length; i++){
            nums[i] = answer[i].intValue();
        }
    }
}