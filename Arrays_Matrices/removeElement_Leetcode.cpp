/*
    Problem: https://leetcode.com/problems/remove-element/
*/

#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        // base case 1: if our array has no elements in it.
        if(nums.size() < 1)
        {
            return 0;
        }
        
        // ---- general algorithm ----
        
        // this variable represents the index where we will next change the element
        // according to the rule below.
        int where_to_change = -1;
        
        for(int i = 0; i < nums.size(); i++)
        {
            
            // once we encounter an element in our array (nums[i]) where != the given value (val)...
            if(nums[i] != val)
            {
                // ... AND i is NOT in the same index we are about to change...
                if(i != where_to_change)
                {
                    where_to_change++;
                    nums[where_to_change] = nums[i];
                }
            }
            
            // skip the values that are == value since we want to overwrite those.
        }
        
        // the size of the 'modified' nums vector/array is = the last index we changed +1!
        return where_to_change+1;
    }
};