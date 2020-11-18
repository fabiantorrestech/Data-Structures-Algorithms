/*
    Problem: 
*/


#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*
    ---- EXPLANATION ----
    
    DATA STRUCTURES & SETUP:
    
    - intialize 2 helper functions to help convert from ascii letters for the 26
      lowercase a-z(ascii values 97-122) --> simple numbers 0-25 (26). Will be useful
      for assigning an incrementer for the arrays below.
        + 1) lc_int_to_letter (ex: a -> 0)
        + 2) lc_letter_to_int (ex: 0 -> a)
    
    - keep 2 arrays of size 26 (indices from 0-25) for each letter in the alphabet.
    - because we are using 2 arr's to talk about the same letters, we'll only use 1 incrementer
      to access both of them at a time usually (i).
        + 1) (repeated[]) - one for if a character has been repeated in given string 's'. 
        + 2) (indices[]) - one for if the noting the 1st index of seen character.
            ... BY CONVENTION WE INIT ALL VALUES IN indices[] to -1 to say 'we haven't seen that character yet'
                if we have seen it, it will be a non-negative value. different from -1.
     
     _______________________________        
    |___|___|___|___|___|___|___|___| ... repeated[]
      ^
      | i
     _V_____________________________        
    |___|___|___|___|___|___|___|___| ... indices[]
    
    ==========================================================================================
    ALGORITHM / SOLUTION:
    
    - first iterate through all characters of the string 's' (the first FOR LOOP)
        + if a character is seen, lets note it by change its value in indices[].
        + if a character has already been seen, we knows its val will be >= 0 @ indices[i].
          ... so now we know that we've seen it again, we can change repeated[i] = true.
        
    - Next we iterate through our 2 arrays, repeated[] and indices[] to check for each letter 
      (the second FOR LOOP)
        + if we have find a letter which has been seen once, not been repeated,
          immediately make it our first answer to compare the rest of the letters to.
            ... BY CONVENTION, if answer = -1, no 'first non-repeating character' in the string
            exists.
        + if we find any other non-repeated AND seen letters, just compare their index values to see
          which index is lower. We want the LOWEST non-repeated & seen index of a character.

    */

// ---- helper functions for converting char ascii ('a'-'z') to an int (0-25) ----
int lc_letter_to_int(char given_char)
{
    return given_char - 'a';
}

int lc_int_to_letter(int given_int)
{
    return given_int + 'a';
}


char firstNotRepeatingCharacter(string s) {
    
    vector<bool> repeated(26, false);   
    vector<int> indices(26, -1);        
    int answer = -1;                    // where we will update our final answer to return.
                                        // (this works fine for returning a char since ascii values cover us)
    
    
    int num = 0;
    for(int i = 0; i < s.size(); i++)
    {
        num = lc_letter_to_int(s[i]);
        
        // s[i] has not been noted at all yet.
        if(indices[num] < 0)
            indices[num] = i;
        
        // have seen it once before, but has not been noted as repeated.
        else if(indices[num] >= 0 && repeated[num] == false)
            repeated[num] = true;

    }
    
    /*
    //test print function
    for(int i = 0; i < repeated.size(); i++)
    {
        cout << "repeated[" << i <<"]: " << repeated[i] << endl;
        cout << "indices[" << i <<"]: " << indices[i] << endl;
    }
    */
    
    bool first_replace = false;
    for(int i = 0; i < repeated.size(); i++)
    {
        // found a letter which has been seen once, not been repeated.
        if(indices[i] != -1 && repeated[i] == false)
        {   
            if(first_replace == false)
            {
                answer = lc_int_to_letter(i);
                first_replace = true;
            }
            
            else if(first_replace == true)
            {
                if(indices[i] < indices[lc_letter_to_int(answer)])
                    answer = lc_int_to_letter(i);
            }
                
        }
        
    }
    
    // need to return if no firstNotRepeatingCharacter exists.
    if (answer == -1)
        return '_';
    
    return answer;
}
