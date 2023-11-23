// problem: https://leetcode.com/problems/binary-search/
// TIME:  O(logn)
// SPACE: O(1)
// - the most optimal solution, implemented with less-than-equal (<=) in Java


class Solution {
    public int search(int[] nums, int target) {
        
        int left = 0;
        int right = nums.length-1;
        while(left <= right){
            int mid = left + (right-left/2); // find the midpoint for the array. (we use +left to prevent overflow.)
            
            if(nums[mid] == target){  // we find the solution.
                return mid;
            }
            else if(nums[mid] < target){ // search on the right half of array for solution
                left = mid+1;
            }
            else if(nums[mid] > target){ // search on the left half of the array for solution.
                right = mid-1;
            }
        }
        
        return -1;
    }
}