/*
    Problem: https://leetcode.com/problems/hamming-distance/
*/


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
int hammingDistance(int x, int y)
{
    int result = 0;
    int hamming = 0;
    for(int i = 0; i < 31; i++){

            // 1) x%2 tells us if the last bit is 0 or 1.
            //
            // 2) result = LEFT ^ RIGHT compares LEFT and RIGHT to check if the bits are different (XOR).
            // 
            // 3)   1st time around if x = 1: 010(1)
            //
            //      - x >> 1 (x's bits are shifted right 1)
            //
            //      2nd time around if x = 5: 001(0)
            //
            // 4) result will tell us if ONLY last bits are different (thanks to modulo)
            //
            // 5) REPEAT THIS FOR ALL 31 bits!
            
            result = (x%2) ^ (y%2);
            
            if(result == 1){
                hamming++;   
            }
            
            x = x>>1;
            y = y>>1;
        }
        
    return hamming;
    }
};