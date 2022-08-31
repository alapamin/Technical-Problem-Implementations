class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #Happy case: O(logn) time comp
        #Worst case: O(n) time comp
        
        #Space: O(1)
        left,right = 0,len(nums)-1
        if len(nums) == 1:
            return False if nums[0] != target else True
        while left <= right:
            mid = left + (right-left) // 2

            
            while nums[left] == nums[right] and left < right:
                left+=1

            
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True
            
            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[mid] and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False