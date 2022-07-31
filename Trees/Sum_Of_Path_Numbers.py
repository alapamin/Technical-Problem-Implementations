class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

#When solving by adding to a global integer value, we returned 0

#When solving by appending the current number to a global array and
#then calculating the sum of that array in the main function -> return correct answer

def find_sum_of_path_numbers(root):
  def dfs(root,cNum,ans):
    if root is None:
      return

    cNum = (cNum*10) + root.val

    if not root.left and not root.right:
      print(cNum)
      ans.append(cNum)
    
    dfs(root.left,cNum,ans)
    dfs(root.right,cNum,ans)

    cNum-=root.val
    cNum/=10

  ans = []
  dfs(root,0,ans)
  return sum(ans)




def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
