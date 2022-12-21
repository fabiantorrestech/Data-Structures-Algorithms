// problem: https://leetcode.com/problems/two-sum/submissions/
// - TIME: O(n^2)
// - SPACE: O(1)
//  - Naive Solution. slightly optimized to do less calculations in the inner for-loop.

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] answer = new int[2];
        for(int i=0; i<nums.length; i++){
            for(int j=i+1; j<nums.length; j++){
                if(nums[i]+nums[j]==target){
                    answer[0]=i;
                    answer[1]=j;
                    return answer;
                }
            }
        }
        
        return answer;
    }
}