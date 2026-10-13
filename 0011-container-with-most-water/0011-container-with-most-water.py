class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_ans = 0
        l, r = 0, len(height) - 1
        while l < r:
            temp = min(height[l], height[r]) * (r - l)
            max_ans = max(temp, max_ans)
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        
        return max_ans
        