# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #res = True
        def dfs(nodep, nodeq):
            #nonlocal res
            if not nodep and not nodeq:
                return True
            if not nodep and nodeq:
                res = False
                return False
            if not nodeq and nodep:
                res = False
                return False
            if nodeq.val != nodep.val:
                res = False
                return False
            
            return dfs(nodep.left, nodeq.left) and dfs(nodep.right, nodeq.right)
        
        return dfs(p,q)

            
        