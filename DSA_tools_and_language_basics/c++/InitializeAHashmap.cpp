// NOT FINISHED!!!!

#include <iostream>
#include <unordered_map>
using namespace std;

int main(){

    // declaration
    unordered_map<string, int> hashmap;

    // insertion
    hashmap["key1"] = 1;
    hashmap["key2"] = 2;
    hashmap["key3"] = 3;

    // printing a hashmap's keys and values
    // - x.first = key
    // - x.second = value
    for(auto x : hashmap){
        cout << "hashmap[" << x.first << "]: " << x.second << endl; 
    }

    // lookup by key

    // delete key
    


    return 0;
}