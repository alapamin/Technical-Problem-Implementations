# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [-1]
        def dfs(root):
            if root is None:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            current = False
            if root == p or root == q:
                current = True
                
            if (left and right) or (current and (left or right)):
                ans[0] = root
            
            return left or right or current
        
        
        dfs(root)
        return ans[0]