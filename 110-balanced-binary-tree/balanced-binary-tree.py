# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        balanced = True

        def dfs(node):
            nonlocal balanced
            if not node:
                return -1

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if abs(left_depth - right_depth) > 1:
                #print("Wow thats not balanced")
                balanced = False

            #print("depth of", node.val, "is", 1 + max(left_depth, right_depth))
            #print("left", left_depth)
            #print("right", left_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return balanced