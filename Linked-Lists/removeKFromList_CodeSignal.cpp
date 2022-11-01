/*
    Problem: https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm/description
*/

#include <iostream>
#include <vector>

// Singly-linked lists are already defined with this interface:
// template<typename T>
// struct ListNode {
//   ListNode(const T &v) : value(v), next(nullptr) {}
//   T value;
//   ListNode *next;
// };
//
ListNode<int> * removeKFromList(ListNode<int> * l, int k) {
    
    // base case is list is empty.
    if(l == NULL)
    {
        return l;
    }
    
    // ---- list must have at least 1 element to get here ----

    ListNode<int>* curr = l;
    ListNode<int>* temp;
    ListNode<int>* prev = NULL;
    bool head_replacement = false;
    
    while(curr != NULL){   
        //cout << "curr->value: " << curr->value << endl;
        
        // head needs to be replaced...
        if(l == curr && prev == NULL && curr->value == k){
            //cout << "head replacement on curr->value: " << curr->value << endl;
            if(curr->next != NULL){
                curr = curr->next;
                l = curr;
                continue;
            }
            // reached end of list.
            else
                return NULL;
                
        }
        
        // intermediate nodes after head need replacing...
        else if(curr->value == k){
            //cout << "general replacement" << endl;
            if(prev != NULL){
                if(curr->next != NULL){
                    curr = curr->next;
                    prev->next = curr;
                    continue;   
                }
                else{
                    curr = curr->next;
                    prev->next = NULL;
                    continue;
                }
            }  
        }
        
        prev = curr;
        curr = curr->next;  
    }
    
    return l;
}
