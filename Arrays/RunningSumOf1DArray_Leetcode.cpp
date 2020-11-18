/*
    Problem: https://leetcode.com/problems/running-sum-of-1d-array/
*/


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
                
        for(int i = 0; i < nums.size(); i++)
        {
            if(i == 0)
                nums[i] = nums[i];
            else
            {
                nums[i] = nums[i] + nums[i-1];
            }
        }
        
        return nums;
    }
};