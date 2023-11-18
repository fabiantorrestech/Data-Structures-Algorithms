// problem: https://leetcode.com/problems/two-sum/
// - TIME: O(n)
// - SPACE: O(n)
//  - THE optimal solution utilizing a hashmap and 1 loops.

class Solution {
    
    public int[] twoSum(int[] nums, int target) {
        
        // populate the hashmap. <k,v> = <nums[idx], idx>
        HashMap<Integer, Integer> numsHM = new HashMap<Integer, Integer>();
        
        for(int i=0; i<nums.length; i++){
            int numToFind = target-nums[i];
            
            if(numsHM.containsKey(numToFind)){
                int ansArray[] = new int[2];
                ansArray[0] = i;
                ansArray[1] = numsHM.get(numToFind);
                return ansArray;
            }
            
            numsHM.put(nums[i], i);
        }
        
        return null; // should never hit here
    }
    
}