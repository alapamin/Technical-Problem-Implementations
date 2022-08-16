from typing import List

#O(logn) time
#O(1) space

def binary_search(arr: List[int], target: int) -> int:
    start,end = 0,len(arr)-1
    while start <= end:
        mid = start + (end-start) // 2
        if target == arr[mid]:
            return mid
        if arr[end] > arr[start]:
            if target < arr[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if target > arr[mid]:
                end = mid-1
            else:
                start = mid+1
    return -1
                    

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)
