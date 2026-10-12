class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        for num in nums:
            stack = []
            while num > 0:
                digit = num % 10
                stack.append(digit)
                num = num // 10
            while stack:
                out.append(stack.pop())
        
        return out