/*
    Problem: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
*/

#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        
        int busy_students=0;
        for(int i = 0; i < startTime.size(); i++)
        {
            if(startTime[i] <= queryTime)
            {
                if(endTime[i] >= queryTime)
                {
                    busy_students++;
                }
            }
        }
        
        return busy_students;
    }
};