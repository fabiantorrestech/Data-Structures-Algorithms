#include <iostream>
#include <map>

using namespace std;

int firstDuplicate(vector<int> a) {
    
    // 2 mainmethods off top of head:
    // 1) utilize a dictionary
    // 2) first sort the array then simply binary search for that element where it belongs and check if any duplicates lie to its left or right.
    //
    // --------------------------
    //
    // Going to use dictionary method 1...
    
    
    std::map<int, int>  numbers; // key - integer (what exact # was seen?)
                                 // val - val (# times seen?)
    
    for(int i=0; i < a.size(); i++)
    {
        if(!numbers.count(a[i]))
        {
            numbers.insert({a[i],1});   // if the number does not exist in our hashmap, add it.
        }
        
        else
        {
            return a[i];        // if it does exist already in the map, then when we find it again,
                                // we have found a duplicate. Furthermore, the first duplicate we find will
                                // already have the lowest index. So simply return the first duplicate
                                // we find. (:
        }
    }
    
    // no duplicates found
    return -1;
}
