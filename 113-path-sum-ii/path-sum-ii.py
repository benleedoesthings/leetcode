# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans = []

        def dfs(node, path, total):
            #print("Calling with", node, path, total)
            nonlocal ans

            if not node:
                #print("No node")
                return

            if not node.left and not node.right:
                if total + node.val == targetSum:
                    #print("Found that sum")
                    #print(path)
                    ans.append(path + [node.val])
                return

            #print("Currently on node", node.val)

            dfs(node.left, path + [node.val], total + node.val)
            dfs(node.right, path + [node.val], total + node.val)
            
        dfs(root, [], 0)

        return ans