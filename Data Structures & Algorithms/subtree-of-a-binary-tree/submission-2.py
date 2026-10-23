# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def compareNodes(p,q):
            if not q and not p:
                return True
            if not p and q:
                return False
            if not q and p:
                return False
            if q.val != p.val:
                return False
            
            return compareNodes(p.left, q.left) and  compareNodes(p.right, q.right)
        def dfs(node):
            if not node:
                return False
            compareRes = compareNodes(node, subRoot)
            return compareRes or dfs(node.left) or dfs(node.right)
        return dfs(root)
            
            
        