# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}
        for i, num in enumerate(inorder):
            inorder_index[num] = i

        curr = -1

        def build(l, r):
            nonlocal curr
            if l > r:
                return None

            #print("l=", l, "r=", r)
            curr += 1

            node = TreeNode(preorder[curr])
            mid = inorder_index[preorder[curr]]

            #print("mid=", mid)

            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)

            return node
        
        tree = build(0, len(preorder) - 1)
        return tree