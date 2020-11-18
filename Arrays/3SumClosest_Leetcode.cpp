/* !!! WARNING: NAIVE SOLUTION WITH 3PTRS !!! */    

/*
Problem: https://leetcode.com/problems/3sum-closest/
*/

#include <iostream>
#include <vector>

#include <cstdlib> // for abs

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        //base case 0: that should never happen acc to prompt?
        if(nums.size() < 3)
            return -1;
        
        //base case 1: nums is only 3 numbers
        if(nums.size() == 3)
            return (nums[0] + nums[1] + nums[2]);
        
        // ----- general algorithm for most cases ----
        int closest_sum = 0;
        bool initial_run = true;
        int answer = 0;
        if(nums.size() > 3)
        {
            for(int i = 0; i < nums.size(); i++)
            {
                for(int j = i+1; j < nums.size(); j++)
                {
                    for(int k = j+1; k < nums.size(); k++)
                    {
                        answer = nums[i] + nums[j] +nums[k];
                        
                        // initial run to set the number to compare all the
                        // rest of our answers to.
                        if(initial_run == true)
                        {
                            closest_sum = answer;
                            initial_run = false;
                            continue;
                        }
                        
                        // we want how far off we are from the target
                        // (specifically the unsigned value)
                        int ans_to_comp = abs(target-answer);
                        int closest_sum_to_comp = abs(closest_sum-target);
                        
                        // replace the closest_sum to the answer
                        // if its distance from the target is
                        // less than current 'closest_sum' value
                        if(ans_to_comp < closest_sum_to_comp)
                            closest_sum = answer;
                        
                    }
                }
            }
            
        }
        
        return closest_sum;
    }
};