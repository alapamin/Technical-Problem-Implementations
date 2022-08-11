#O(n) time
#O(1) space
#Assuming sorted array input
def pair_with_targetsum(arr, target_sum):
  left,right = 0,len(arr)-1
  while left < right:
    leftN,rightN = arr[left],arr[right]
    cSum = leftN + rightN
    if cSum < target_sum:
      left+=1
    elif cSum > target_sum:
      right-=1
    else:
      return [left,right]