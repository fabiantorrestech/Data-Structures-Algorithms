import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        // intialize a hashmap -> <k,v> == <num, idx> 
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        
        int[] answer = new int[2];
            
        // go through nums once and store all numbers in hm
        for(int i=0; i<nums.length; i++){
            hm.put(Integer.valueOf(nums[i]), Integer.valueOf(i));
        }
        
        
        for(int i=0; i<nums.length; i++){
            Integer desiredNum = target-nums[i];  // a+b=target --> target-a=b (b is number to look for)
            
            // if its in HM, then it will not return 'null'
            if(hm.containsKey(desiredNum) &&
               hm.get(desiredNum) != Integer.valueOf(i)){
                answer[0]=i;
                answer[1]=Integer.valueOf(hm.get(desiredNum));
                return answer;
            }
        }
        
        return answer;
    }
}