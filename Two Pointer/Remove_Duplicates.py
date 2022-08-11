def remove_duplicates(arr):
  count = 0
  left,right = 0,1
  while right < len(arr):
    if arr[left] != arr[right]:
      count+=1
    left+=1
    right+=1
  return count+1 if count != 0 else 0
