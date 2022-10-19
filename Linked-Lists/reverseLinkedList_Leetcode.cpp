/*
    Problem: https://leetcode.com/problems/reverse-linked-list/
*/

#include <iostream>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        ListNode* prev = NULL;
        ListNode* future = NULL;
        ListNode* curr = head;
        
        while(curr != NULL){
            future = curr->next;    // preserve curr.next 
            curr->next = prev;      // reroute curr.next to prev (reversing)
            prev = curr;            // move prev up to curr's position
            curr = future;          // move curr up to future's position
        }
        
       
        return prev;  // prev is now new 'head' of reversed-LL
    }
};