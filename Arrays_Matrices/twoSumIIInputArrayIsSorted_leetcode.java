// problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// TIME: O(logn)
// SPACE: O(1)
// - optimal solution implemented in Java via 2 pointers. Answer is indices+1, since the array is meant to be 1-indexed.

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        int left = 0;
        int right = numbers.length-1;
        int[] ans = new int[2];
        while(left < right){
            int sum = numbers[left]+numbers[right];
            
            // found our 2 numbers that add up to target
            if(sum == target){
                ans[0] = left+1;
                ans[1] = right+1;
                return ans;
            }
            // shift our left pointer to right bc target is MORE
            else if(sum < target)
                left++;
            // shift our right pointer to left bc target is LESS
            else
                right--;
        }
        
        // will never reach here.
        return null;
    }
}