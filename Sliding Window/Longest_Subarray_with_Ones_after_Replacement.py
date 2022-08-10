#O(n) time
#O(1) space, no hashmap needed just a counter variable and maxSize variable. (both are ints)
def length_of_longest_substring(arr, k):
  if not arr:
    return 0
  windowStart,winMax,zeros = 0,float('-inf'),0

  for windowEnd in range(len(arr)):
    if arr[windowEnd] == 0:
      zeros+=1
    while zeros > k and windowStart < windowEnd:
      if arr[windowStart] == 0:
        zeros-=1
      windowStart+=1
    winMax = max(winMax,windowEnd-windowStart+1)
  
  return winMax
