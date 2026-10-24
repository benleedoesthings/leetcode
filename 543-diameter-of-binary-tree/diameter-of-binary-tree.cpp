/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    // int diameterOfBinaryTree(TreeNode* root) {
    //     int rightLongest = diameterHelper(root->right);
    //     int leftLongest = diameterHelper(root->left);
    //      cout << "left: " << leftLongest<<endl;
    //      cout << "right: " << rightLongest<<endl;

    //     int combo = rightLongest + leftLongest + 1;

    //     if (rightLongest > combo) return rightLongest;
    //     else if (leftLongest > combo) return leftLongest;
    //     else return combo;

    // }

    // int diameterHelper(TreeNode* root) {
    //     if(root == nullptr) {
    //         return 0;
    //     }
        
    //     int leftHeight = diameterHelper(root->left);
    //     int rightHeight = diameterHelper(root->right);
        
    //     int height = max(leftHeight, rightHeight) + 1;
        
    //     // cout << "getting " << root->val << endl;
    //     // cout << "height is " << height << endl;

    //     return height;
    // }
    
    
    int diameterOfBinaryTree(TreeNode* root) {
        pair<int, int> rightLongest = diameterHelper(root->right);
        pair<int, int> leftLongest = diameterHelper(root->left);

        int combo = rightLongest.first + leftLongest.first;
        int rightSubtree = rightLongest.second;
        int leftSubtree = leftLongest.second;
        
        cout << "combo: " << combo <<endl;
        cout << "rightSubtree: " << rightSubtree << endl;
        cout << "leftSubtree: " << leftSubtree <<endl;
        
        return max({combo, rightSubtree, leftSubtree});

    }

    pair<int, int> diameterHelper(TreeNode* root) {
        if(root == nullptr) {
            return {0, 0};
        }
        
        pair<int, int> leftHeight = diameterHelper(root->left);
        pair<int, int> rightHeight = diameterHelper(root->right);
        
        int height = max(leftHeight.first , rightHeight.first) + 1;
        int maxSubTreePathPossible = leftHeight.first + rightHeight.first;
        int maxSubTreePath = max({maxSubTreePathPossible, leftHeight.second, rightHeight.second});
        
        
        cout << "node: " << root->val<<endl;
        cout << "height: " << height << endl;
        cout << "maxSubtree: " << maxSubTreePath <<endl;
            
        return {height, maxSubTreePath};
    }
};