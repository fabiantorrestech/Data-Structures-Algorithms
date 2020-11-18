#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    bool isHappy(int n) {
        
        // base case; if its 0, it will never be happy (:
        if(n == 0)
        {
            return false;
        }
        
        
        vector<int> seen_before;    // a vector of answers we've computed before from an
                                    // iteration of this outer while loop.
        
        int num = 0;                // extracted digit from 'n'
        int num_sq = 0;             // extracted digit from 'n', squared.
        vector<int> digits;         // for each extracted digit 
        int answer = 0;
        
        // keep trying this until we hit 1, which means its happy!
        while(answer != 1)
        {
            answer = 0;
     
            // 1) extract the digits from n, square it, then push it into 'digits' vector.
            while(n>0)
            {
                num = n%10;
                num_sq = num * num;
                digits.push_back(num_sq);
                n = n/10;
            }
            
            // 2) add the squared digits up as our answer.
            for(int i = 0; i < digits.size(); i++)
            {
                answer = answer + digits[i];
            }
            
            // 3) Observe:
            // - All numbers that are NOT happy repeat a cycle when we do this.
            // - So IF WE NOTICE WE GET NUMBERS THAT WE'VE ALREADY GOTTEN before,
            //   we can end it and conclude that its not a happy number.
            // - If the number is happy, it will eventually hit 1.
            for(int i = 0; i < seen_before.size(); i++)
            {
                if(seen_before[i] == answer)
                {
                    return false;
                }
            }
            
            // 4) Clean up work
            // - Store the answer we've seen because its unique.
            // - clear the digits vector for extracted digits.
            // - set n = answer to run loop again.
            seen_before.push_back(answer);
            digits.clear();
            n = answer;
        }
        
       return true;
    }
};