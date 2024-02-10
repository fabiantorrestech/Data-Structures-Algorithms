// problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// TIME: O(logn)
// SPACE: O(1)
// - optimal solution implemented in Java via 2 pointers. Answer is indices+1, since the array is meant to be 1-indexed.

class Solution {
    public int[] twoSum(int[] numbers, int target) {
    
        int[] ans = new int[2];
        int left=0, right=numbers.length-1;
        while(left < right){
            int result = numbers[left] + numbers[right];
            if(result<target)
                left++;
            else if(result>target)
                right--;
            else
                break;
        }
        ans[0]=left+1;
        ans[1]=right+1;

        return ans;
    }
}