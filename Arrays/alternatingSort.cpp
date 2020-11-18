#include <vector>
#include <iostream>

bool alternatingSort(vector<int> a) {
    
    int left = 0;
    int right = a.size()-1;
    vector<int> b;
    bool answer = true;
    
    
    // create arr b[]
    bool left_turn = true;
    bool right_turn = false;
    while(left <= right)
    {
        //left first, then right
        if(left_turn)
        {
            b.push_back(a[left]);
            left++;
            right_turn = true;
            left_turn = false;
        }
        else if(right_turn)
        {
            b.push_back(a[right]);
            right--;
            right_turn = false;
            left_turn = true;
        }
    }
    
    /*
    for(int i = 0; i < b.size(); i++)
    {
        cout << "b[" << i << "]: " << b[i] << endl;
    }
    cout << endl;
    */
    
    
    // now check if that array is sorted properly...
    for(int i = 0; i < b.size(); i++)
    {
        // cant compare yet...
        if(i == 0)
            continue;
        
        // general algo (NEEDS to be strictly ascending)
        else if(b[i-1] >= b[i])
        {
            /*
            cout << "b[" << i-1 << "]: " << b[i-1] << endl;
            cout << "b[" << i << "]: " << b[i] << endl;
            cout << endl;
            */
            return false;
        }
    }
    
    
    return answer;
}
