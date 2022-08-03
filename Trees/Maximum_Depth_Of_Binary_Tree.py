# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #compare depth to max depth -> set if greater 
        #Traverse down tree via DFS -> pass in depth + 1
        #O(n) time 
        #O(n) space (recursion stack)
        self.depth = 0
        def dfs(root, d):
            if root is None:
                return 0
            
            dfs(root.left,d+1)
            dfs(root.right,d+1)
            
            self.depth = max(self.depth,d)
            
        dfs(root,0)
        return self.depth+1 if root else 0
        
        