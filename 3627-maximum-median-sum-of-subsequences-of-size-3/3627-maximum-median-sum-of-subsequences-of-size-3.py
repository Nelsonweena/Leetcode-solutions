class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = 0

        groups = len(nums) // 3

        for i in range(groups):
            ans += nums[r - 1]

            r -= 2 
            l += 1
        
        return ans