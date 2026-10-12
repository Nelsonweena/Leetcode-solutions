class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l = len(nums)
        ans = 0
        for j in range(l):
            if l % (j + 1) == 0:
                ans += nums[j]**2
        
        return ans