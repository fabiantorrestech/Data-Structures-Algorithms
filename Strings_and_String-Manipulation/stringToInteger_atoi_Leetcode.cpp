/*
    Problem: https://leetcode.com/problems/string-to-integer-atoi/
*/

/* !!! WARNING: messy solution !!! */    

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int myAtoi(string str) {

        // not valid conversion = return 0
        // valid conversion  = return result
        
        vector<int> number_digits;
        double result = 0;
        int pow_result = 0;
        bool is_negative = false;
        bool is_positive = false;
        bool space_after_digits = false;
        
        for(int i = 0; i < str.size();i++){
            
            // if its a number
            if(isdigit(str[i]) == 1){
                number_digits.push_back(str[i] - '0');
                pow_result++;
            } 
            
            //otherwise, investigate...
            else{
                
                if(is_negative == 1){
                    if(isdigit(str[i]) != 1){
                        break;
                    }
                }
                
                if(is_positive == 1){
                    if(isdigit(str[i]) != 1){
                        break;
                    }
                }
                
                // if space dont count it.
                else if(str[i] == ' '){
                    if(number_digits.empty() == true){
                        continue;   
                    }
                    else{
                        break;
                    }
                }
                
                else if(str[i] == '+'){
                    is_positive = true;
                    continue;
                }
                
                // if negative
                else if(str[i] == '-'){
                    
                    if(number_digits.empty() == false){
                        break;
                    }
                    
                    is_negative = true;
                    cout << "is negative!" << endl;
                    continue;
                }
                
                // if its a letter, stop reading.
                else if(isalpha(str[i])){
                    cout << "test!" << endl;
                    cout << str[i] << endl;
                    break;
                }
                
                // truncate at a decimal
                if(str[i] == '.'){
                    break;
                }
                
                /// if it reaches this pt, its not a num or any above cases at the first char. return 0.
                if(i == 0){
                    return 0;
                }
                
            }
            
            
        }
        
        if(is_negative == 1 && is_positive == 1){
            return 0;
        }
        
        if(number_digits.empty() == 1){
            return 0;
        }
        
        
        //put that number together.
        for(int i = 0; i < number_digits.size(); i++){
                result = result + (number_digits[i] * pow(10, pow_result-1));
                cout << number_digits[i] << endl;
                cout << "result:" <<  result << endl;
                pow_result--;
        }
        
        if(is_negative == true){
            result = result * -1;
        }
        
        if(result <= -2147483648){
            return -2147483648;
        }
        
        if(result >= 2147483648){
            return 2147483647;
        }
        
        cout << result;
        int answer = 0;
        answer = int(result);
        cout << answer;
        
        return answer;
    }
};