#include <iostream>

struct TreeNode
{
    int val;
    TreeNode* left;
    TreeNode* right;
};


void in_order_print(TreeNode* root)
{
    if(root == NULL)
        return;
    else
    {
        in_order_print(root->left);
        printf("%d ", root->val);
        in_order_print(root->right);
    }
}

int main()
{
    // give this function the root of a tree and it will print it, in order
    in_order_print();
}