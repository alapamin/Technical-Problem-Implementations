# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #for every node in root tree check if the tree from the node is the same as subRoot -> if any are -> return true
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        answer = True
        finalAns = False
        def isSame(root,subRoot):
            nonlocal answer
            if root is None and subRoot is None:
                return
            if root is None or subRoot is None:
                answer = False
                return
            
            if root.val != subRoot.val:
                answer = False
            
            isSame(root.left,subRoot.left)
            isSame(root.right,subRoot.right)
            
        
        def dfs(root,subRoot):
            nonlocal finalAns
            nonlocal answer
            if root is None:
                return
            
            answer = True
            isSame(root,subRoot)
            if answer:
                finalAns = True
            
            left = dfs(root.left,subRoot)
            right = dfs(root.right,subRoot)

            
                
        dfs(root,subRoot)
        return finalAns
            
                
            