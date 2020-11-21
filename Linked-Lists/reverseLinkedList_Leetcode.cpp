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
        
        // to reverse a singly linked list, we'll need to create a previous node to
        // remember our predecessor. Then we can just reroute our node's "next" ptr
        // so that we can traverse it from beginning to end!
        //
        // ex: 1 -> 2 -> 3 -> 4 -> 5 -> NULL     NORMAL
        //
        //     5 -> 4 -> 3 -> 2 -> 1 -> NULL     REVERSED
        //
        //  curr = current node we're at for current iteration.
        //  prev = previous node for the next iteration we want to look back at.
        //  future = current->next for current iteration.
        //
        // this can be quite confusing to wrap your head around. suggested to draw this out
        // and do a few examples on a whiteboard or on paper...
        
        if(head == NULL)
            return NULL;
        
        ListNode* prev;
        ListNode* future;
        ListNode* curr = head;
        while(curr != NULL)
        {   
            if(curr == head)
                prev = NULL;
            
            future = curr->next;
            curr->next = prev;
            prev = curr;
            curr = future;
        }
        
        // want to return prev since our curr is at NULL now (while loop condition)
        return prev;
    }
};