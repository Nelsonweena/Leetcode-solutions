class Solution(object):
    def minOperations(self, nums, k):
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

        if(sum == k):
            return 0
        
        return sum % k
        