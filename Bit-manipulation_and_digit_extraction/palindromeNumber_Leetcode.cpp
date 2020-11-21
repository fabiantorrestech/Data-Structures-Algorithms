#include <iostream>

class Solution {
public:
    bool isPalindrome(int x) {
        
        // a palindrome is a number that is the same forwards --> and backwards <--
        // ex: 112211, 9009, 515, 66
        //
        // ---- general algorithm ----
        //
        // 1) extract digits and store them in a vector. (right-to-left <--- operation)
        //
        //      - to isolate the last digit on each iteration, use % operator to grab remainder.
        //      - to keep x moving along to the right, need to divide x/10.
        //      - once x/10 is not >= 1, just store the last digit x.
        //
        // 
        //      (ex: 110              Note: SAVE = store digit in ANSWER                )
        //
        //           loop iterations:
        //              110%10 = 0 (SAVE THIS) -> 110/10 = 11.0
        //              11%10  = 1 (SAVE THIS) -> 11/10 = 1.1 (int truncates .1) = 1.0
        //              1/10   = 0.1 (int truncates .1) = 0 ... which is < 1 ...
        //                       ... so the general 'else' statment in loop will not execute...
        //                            INSTEAD just take x and add it to our result.
        //
        //
        // 2) now just compare your given number (x) and the one you constructed by extracting digits...
        //      - if SAME, then its a palindrome
        //      - if diff, then NOT a palindrome.
        // 
        // =====================================================================================
        
        // BASE CASE 1: will be true for NON-negative single digit numbers.
        if(x > -1 && x < 10)
            return true;
        
        // BASE CASE 2: will be false for negative numbers due to negative sign...
        // ex: -121 backwards is 121- which is NOT a valid palindrome...
        if(x < 0)
            return false;
        
        // 1) extract digits and reconstruct number.
        int digit = 0;
        long answer = 0;
        int x_copy = x;
        while(x != 0)
        {
            // for last case digit where x/10 is too small to use modulo...
            if(x/10 < 1)
                digit = x;
            
            // general case.
            else
                digit = x%10;
            
            answer = answer*10 + digit;
            x = x/10; 
        }
        
        // 2) compare the reconstructed number and given number
        if(answer == x_copy)
            return true;
        
        
        return false;
    }
};