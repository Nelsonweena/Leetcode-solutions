class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > 9 * num or sum < 1:
            return ""

        ans = ""

        for i in range(num):
            digit = min(9, sum)
            ans += str(digit)
            sum -= digit

        return ans