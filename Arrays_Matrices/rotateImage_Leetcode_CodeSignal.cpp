/*
    Problem: https://leetcode.com/problems/rotate-image
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    
    void print_grid(vector<vector<int>>& matrix)    // helper for printing the grid
    {
        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix.size(); j++){
                cout << matrix[i][j] << "  |  "; 
            }
            cout << endl;
        }    
        cout << endl;
    }
    
    void rotate(vector<vector<int>>& matrix) {
        
        // --- general algorithm ---
        //
        // 1) Transpose matrix; means, we perform 'swap(matrix[i][j], matrix[j][i])'
        // - ONLY DO IT for the top half of the grid since swapping for evrey element will give us same matrix back in the code (j=i)
        // - Time Complexity - O(n/2)
        // - Space Complexity - O(1) since inplace swapping with 1 temp for the swap.
        //
        // 2) Flip the columns of the matrix; we perform swap(matrix[i][j], matrix[i][N-1-j] )
        // - only do it up until halfway of the grid since like above, if we do this for the whole thing, we will be swapping too much...
        // - Time Complexity - O(n/2)
        // - Space Complexity - O(1) since inplace swapping with 1 temp for the swap (reusing from 1) for the swap)
        //
        // Total Time Complexity = O(n/2) + O(n/2) = O(n)
        // Total Space Complexity = O(1)

        //print_grid(matrix);
        int temp;
        for(int i = 0; i < matrix.size(); i++)
        {
            for(int j=i; j < matrix.size(); j++)
            {
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        //print_grid(matrix);
        
        // now swap the columns
        // i = rows
        // j = columns
        for(int i = 0; i < matrix.size(); i++)
        {
            for(int j=0; j < matrix.size()/2; j++)
            {
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][(matrix.size()-1) - j];
                matrix[i][(matrix.size()-1) - j] = temp;
            }
        }
        //print_grid(matrix);
    }
};