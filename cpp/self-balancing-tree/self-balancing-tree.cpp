#include <algorithm>

// Run in C++14.

inline int get_height(node* root = nullptr) 
{
    if(!root) 
        return -1;
    
    return root->ht;
}

inline int get_balance(node* root = nullptr)
{
    return get_height(root->left) - get_height(root->right);
}

node* left_rotate(node* leftNode = nullptr) 
{
    node* rightNode = leftNode->right;
    node* rightLeftNode = rightNode->left;
    
    rightNode->left = leftNode;
    leftNode->right = rightLeftNode;
    
    leftNode->ht = max(get_height(leftNode->left), get_height(leftNode->right)) + 1;
    rightNode->ht = max(get_height(rightNode->left), get_height(rightNode->right)) + 1;
    
    return rightNode;
}

node* right_rotate(node* rightNode = nullptr) 
{
    node* leftNode = rightNode->left;
    node* leftRightNode = leftNode->right;
    
    leftNode->right = rightNode;
    rightNode->left = leftRightNode;
    
    rightNode->ht = max(get_height(rightNode->left), get_height(rightNode->right)) + 1;
    leftNode->ht = max(get_height(leftNode->left), get_height(leftNode->right)) + 1;
    
    return leftNode;
}

node* insert(node* root = nullptr, int val = 0) 
{
    if (root == nullptr) {
        root = new node();
        root->val = val;
        root->ht = 0;
        return root;
    }
    
    if(root->val > val) 
        root->left = insert(root->left, val);
    else if(root->val < val)
        root->right = insert(root->right, val);
    else
        return root;
    
    root->ht = std::max(get_height(root->left), get_height(root->right)) + 1;
    
    const int balance = get_balance(root);

    if (balance > 1 && val < root->left->val)
        return right_rotate(root);
    
    if (balance < -1 && val > root->right->val)
        return left_rotate(root);
    
    if (balance > 1 && val > root->left->val) {
        root->left = left_rotate(root->left);
        return right_rotate(root);
    }
    
    if (balance < -1 && val < root->right->val) {
        root->right = right_rotate(root->right);
        return left_rotate(root);
    }
    
    return root;
}


