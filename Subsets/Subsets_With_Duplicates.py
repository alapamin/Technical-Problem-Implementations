def find_subsets(nums):
  subsets = [[]]
  nums.sort()
  prev = float('inf')
  for j in range(len(nums)):
    cLength = len(subsets)
    if nums[j] != prev: 
      for i in range(cLength):
        subsets.append(subsets[i] + [nums[j]])
    else:
      start = 2**(j-1)
      for i in range(start,cLength):
        subsets.append(subsets[i] + [nums[j]])
    prev = nums[j]
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
