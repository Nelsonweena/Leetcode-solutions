class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        count = [0] * 30

        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    count[i] += 1
        
        ans = 0
        for _ in range(k):
            x = 0
            for i in range(30):
                if count[i] > 0:
                    x += (1 << i)
                    count[i] -= 1

            ans += x * x
        
        return ans % (10**9 + 7)
