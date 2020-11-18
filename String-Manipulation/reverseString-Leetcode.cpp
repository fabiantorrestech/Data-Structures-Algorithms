/*
    Problem: https://leetcode.com/problems/reverse-string/
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {

        // base case: just return the string if its only 1 char or less.
        if(s.size() < 2)
        {
            return;
        }
        
        // GENERAL ALGORITHM:
        // - to revese an array the easiest way, put one ptr at the end
        // and one at the beginning and just simply decrement the end
        // and increase the beginning ptr.
		
		// 1) store either s[end] or s[start] into the temp so you don't lose it! (ill use s[end] for this ex)
		// 2) replace s[end] with s[start]!
		// 3) now where can we find s[end]'s old value since we just overwrote it? thats right, our 'temp' held onto it for us!
		//     replace s[start] with temp
		//  4) continute to do this until our start incremeneter is at the same spot as our end decrementer 
		//      OR until the start has surpassed our end.

		// once they pass eachother up, you know you don't need to swap elements
		// anymore, otherwise you'd be touching more than just the 'n' elements present in
		// the string/array!
		
		//
        
        int start = 0;
        int end = s.size()-1;
        char temp;
        while(start < end)
        {
            temp = s[end];
            s[end] = s[start];
            s[start] = temp;
            start++;
            end--;
        }
        
    }
};