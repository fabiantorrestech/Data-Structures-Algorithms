// problem: https://leetcode.com/problems/rotate-array/
// - TIME: O(n)
// - SPACE: O(1)
//      - optimal solution if you cant use Collections library.

import java.util.Arrays;
// to print an array use "java Arrays.toString(arr)"
//  - ex: System.out.println(Arrays.toString(arr))

class Solution {
    
    // reverses given array IN-PLACE
    public void reverseArray(int[] nums, int l, int r){
        int temp = 0;
        while(l<r){
            temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
    }
    
    public void rotate(int[] nums, int k) {
        
        if(k > nums.length){
            k = k%nums.length;
        }      
        
        // reverse the entire array once
        this.reverseArray(nums, 0, nums.length-1);
        
        // reverse only the first [0,k-1] elements
        this.reverseArray(nums, 0, k-1);
        
        // now reverse the last [k, n] elements
        this.reverseArray(nums, k, nums.length-1);
    }
}