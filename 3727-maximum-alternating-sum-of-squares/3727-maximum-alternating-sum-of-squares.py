class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=abs)

        l,r = 0, len(nums) - 1
        ans = 0

        while l < r:
            ans += nums[r] ** 2
            ans -= nums[l] ** 2
            l += 1
            r -= 1
        
        if r == l:
            ans += nums[l] ** 2
        return ans