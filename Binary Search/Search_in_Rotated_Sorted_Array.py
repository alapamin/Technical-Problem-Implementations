class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Think of IS THE LEFT ARRAY SORTED? OR IS THE RIGHT ARRAY SORTED? we operate based on what we know to then be guaranteed.
        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if target <= nums[mid] and target >= nums[left]:
                    right = mid - 1
                    
                else:
                    left = mid + 1
            else:
                if target >= nums[left] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1