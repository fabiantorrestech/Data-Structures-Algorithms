// problem: https://leetcode.com/problems/find-the-duplicate-number/
// TIME: O(n)
// SPACE: O(n)
// - essentially the same as using a hashmap to solve this problem, but instead we use a set to solve this specifically.

class Solution {
    public int findDuplicate(int[] nums) {
        
        // initalize a hashset to save all seen numbers.
        HashSet<Integer> seenNumbers = new HashSet<Integer>();
        
        for(int i = 0; i < nums.length; i++){
            if(seenNumbers.contains(nums[i]))
                return nums[i];
            seenNumbers.add(nums[i]);
        }
        return 0;
    }
}