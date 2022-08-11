#O(n) time - reversed ans and iteraded through nums array once.
#O(n) space - ans array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        left,right = 0,len(nums)-1
        while left <= right:
            lVal = abs(nums[left])
            rVal = abs(nums[right])
            
            if lVal > rVal:
                ans.append(lVal*lVal)
                left+=1
            else:
                ans.append(rVal*rVal)
                right-=1
                
        return ans[::-1]