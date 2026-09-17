# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, target):
            #print("node=", node.val if node else None)
            if not node:
                return False

            if node.val == target:
                #print("Checking equality")
                if equal(node, subRoot):
                    #print("It's so true")
                    return True

            return dfs(node.left, target) or dfs(node.right, target)

        def equal(node1, node2):
            if node1 and not node2 or not node1 and node2:
                return False

            if not(node1 and node2):
                return True

            if node1.val != node2.val:
                return False

            return equal(node1.left, node2.left) and equal(node1.right, node2.right)

        return dfs(root, subRoot.val)