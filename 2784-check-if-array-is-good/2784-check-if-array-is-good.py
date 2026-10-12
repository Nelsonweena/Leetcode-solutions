class Solution(object):
    def isGood(self, nums):
        n = max(nums)

        if len(nums) != n + 1:
            return False

        nums.sort()

        base = list(range(1, n+1))
        base.append(n)

        return nums == base 