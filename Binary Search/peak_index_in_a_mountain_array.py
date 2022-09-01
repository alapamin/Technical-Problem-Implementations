class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        #O(logn) time, O(1) space
        
        #If the element to the right of mid is >= mid -> move left up 
        #else this means the element to our right is LESS than the middle element, so update answer and move right down
        
        highestIndex = -1
        left,right = 0,len(arr)-1
        
        while left <= right:
            mid = left + (right-left) // 2
            if arr[mid+1] >= arr[mid]:
                left = mid + 1
            else:
                highestIndex = mid
                right = mid - 1
        return highestIndex