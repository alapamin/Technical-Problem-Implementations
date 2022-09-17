class Solution:
    def climbStairs(self, n: int) -> int:
        #O(n) time
        #O(n) space
        memo = {}
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3
        
        def climb(n):
            if n in memo:
                return memo[n]
            
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
        
        return climb(n)