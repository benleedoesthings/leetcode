# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        # I love binary search trees
        # I love binary search trees
        # If I repeat this enough I will solve this problem
        ans = 0

        def inorder(node):
            nonlocal ans
            if node.left:
                inorder(node.left)

            if low <= node.val <= high:
                ans += node.val

            if node.right:
                inorder(node.right)

        inorder(root)
        return ans