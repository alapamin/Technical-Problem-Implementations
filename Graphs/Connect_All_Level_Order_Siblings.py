from __future__ import print_function
from collections import deque

#Time: O(n)
#Space: O(n) where we may have at most n/2 nodes in the queue at the last layer of the tree.
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  if root is None:
    return None
  prev = None
  q = deque()
  q.append(root)
  while q:
    levelSize = len(q)
    for _ in range(levelSize):
      cN = q.popleft()
      if prev:
        prev.next = cN
      if cN.left:
        q.append(cN.left)
      if cN.right:
        q.append(cN.right)
      prev = cN
  prev.next = None



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()
