vector<int> mutateTheArray(int n, vector<int> a) {
    
    // array of size n (a[n])
    // - a[n] -> b[n]
    // - 0 to n-1: b[n] = a[i-1] + a[i] + a[i+1]
    //   + if a[i-1] or a[i+1] DNE, it should be 0.
    
    vector <int> b;
    
    for(int i = 0; i < a.size(); i++)
    {
        // leftmost end of arr
        if(i == 0)
        {
            b.push_back(0 + a[i] + a[i+1]); 
        }
        
        // rightmost end of arr
        else if(i == a.size()-1)
        {
            b.push_back( a[i-1] + a[i] + 0); 
        }
        
        // general algo in middle of arr
        else
        {
            b.push_back(a[i-1] + a[i] + a[i+1]); 
        }
    }
    
    return b;
}
