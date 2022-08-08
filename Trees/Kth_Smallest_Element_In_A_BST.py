# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#O(n) time
#O(h) space -> h is the height of the tree -> worst case O(n) in unbalanced tree
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []
        def inOrderTraversal(root):
            if root is None:
                return
            
            inOrderTraversal(root.left)
            inOrder.append(root.val)
            inOrderTraversal(root.right)
            
        #[1,2,3]
        #3rd smallest -> 
        inOrderTraversal(root)
        if k > len(inOrder):
            return -1
        else:
            return inOrder[k-1]