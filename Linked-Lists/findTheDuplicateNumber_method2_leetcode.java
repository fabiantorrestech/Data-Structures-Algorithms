// problem: https://leetcode.com/problems/find-the-duplicate-number/
// TIME: O(n)
// SPACE: O(n)
// - We use a hashmap to keep track of already seen numbers. then we we query for a number in the hashmap that comes back with a valid entry, 
//   we then know that we've reached the duplicate number. (NOT LINKED LIST implementation)


class Solution {
    public int findDuplicate(int[] nums) {
        
        // use hashmap to keep track of seen numbers.
        // - <k,v> => <number, index>
        HashMap<Integer, Integer> numsHm = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < nums.length; i++){
            // if there is already an entry for this number, then we have found the duplicate.
            if(numsHm.get(nums[i]) != null)
                return nums[i];
            numsHm.put(nums[i], i);
        }
            
        
        return 0;
    }
}