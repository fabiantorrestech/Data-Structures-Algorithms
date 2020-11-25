
/*
Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
*/

#include <iostream>
#include <vector>

using namespace std;


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    
    //notes: 
    // - when given an array passed with a ptr (ex: int* nums) INSTEAD of brackets... (ex: int nums[])
    // - * ("pointer to") is dereference operator to reveal the value (for printing)
    // - & ("address of") is the REFERENCE operator to show the memory address.
    
    // ---------------------------------------
    
    // declare an array with malloc of size 2. (READ ABOVE, returned array must be 'malloced'!!!!)
	// idk why they give us the returnSize since it will always be 2 lol, but i set it to 2 anyway.
    *returnSize = 2;
    int* answer = (int*) malloc(2*sizeof(int));
    answer[0] = -1;
    answer[1] = -1;
    
    // base case 1: we're given an empty array 'nums'
    if(numsSize == 0)
    {
        return answer;
    }
    
    //base case 2: given an array with 1 element, AND the target is THAT 1 element
    if(numsSize==1 && *nums == target)
    {
        answer[0] = 0;
        answer[1] = 0;
        return answer;
    }
    
    // ----the general algorithm---
    
    // to do this in logn time for a sorted array, use binary search!
    // once we find 1 occurence of the target with binary search, spread out left and right
    // with two ptrs (ans_lo) and (ans_hi) FROM 'mdpt' to find the first and last occurences of
	// 'target' in the array 'nums' if target exists
    // 
    // if target DNE in 'nums', we will exhaust the outer while loop condition where lo
	// becomes >= hi.
    
    int lo = 0;
    int hi = numsSize-1;
    int mdpt = (lo + hi)/2;
    bool done = false;
    
    int ans_lo = mdpt;
    int ans_hi = mdpt;
    
    
    // the base case for any binary search recursive call.
    while(lo <= hi)
    {   
        // if the target is smaller than where we are currently at...
        // shrink our problem size by 1/2!
        if(target < *(nums + mdpt))
        {
            hi = mdpt-1;
            mdpt = (lo + hi)/2;
        }
        
        // if the target is greater than where we are currently at...
        // shrink our problem size by 1/2!
        else if(target > *(nums + mdpt))
        {
            lo = mdpt+1;
            mdpt = (lo+hi)/2;
        }
        
        // DING! We've hit the target. Now begins the real problem they're asking for...
        else if(target == *(nums + mdpt))
        {
            // set the 1st (ans_lo) and last (ans_hi) occurences = mdpt, since we are sure of its presence at
            // at LEAST 1 location. we'll update if we see another occurence.
            ans_lo = mdpt;
            ans_hi = mdpt;
            
            // booleans to trigger the 'done' booelan.
            // -if we run through an occurence of this loop where we haven't changed anything, there is nothing
            //  else to do. just stop running through the loop.
            bool ans_lo_change = false;
            bool ans_hi_change = false;
            
            // move our left and right ptrs (ans_lo & ans_hi) until we've seen all occurences of 'target'
            while(!done)
            {
                ans_lo_change = false;
                ans_hi_change = false;
                
                // 1) check any occurences to the left w/ ans_lo (with outer boundary checks first)
                if(ans_lo-1 >= 0 && ans_lo-1 <= numsSize-1)
                {
                     if( *(nums+ans_lo-1) == target ) 
                    {
                        ans_lo = ans_lo - 1;
                        ans_hi_change = true;
                    }
                }
               
                // 2) check any occurences to the right w/ ans_lo (with outer boundary checks first)
                if(ans_hi+1 <= numsSize-1 && ans_hi+1 >= 0)
                {
                    if(*(nums+ans_hi+1) == target)
                    {
                        ans_hi = ans_hi + 1;
                        ans_hi_change = true;
                    }
                }
                
                // 3) if the above checks fail, we're done here!
                if( ans_lo_change==false && ans_hi_change==false )
                { 
                    done = true;
                }
            }
        }
        
        // if we're done, we can break out of the loop w/o doing anymore checks.
        // simply set our answer array to what we've found and just return it.
        if(done)
        {
            answer[0] = ans_lo;
            answer[1] = ans_hi;
            break;
        }

    }
    
    return answer;
}
