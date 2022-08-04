# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        def dfs(root):
            if root is None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            current = max(left,right) + 1
            
            if len(arr) >= current+1:
                arr[current].append(root.val)
            else:
                arr.append([root.val]) 
            
            return current
        dfs(root)
        return arr