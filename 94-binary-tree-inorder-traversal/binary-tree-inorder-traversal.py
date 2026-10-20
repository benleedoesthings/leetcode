# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        def pr(stack):
            st = ""
            for item in stack:
                st += str(item.val) + " "
            return st

        stack = []
        ans = []

        curr = root

        while stack or curr:
            # keep going left as much as you can
            while curr:
                stack.append(curr)
                curr = curr.left

            # pop the last one
            popped = stack.pop()
            ans.append(popped.val)

            # move to the right now
            curr = popped.right

        return ans