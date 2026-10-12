import heapq

class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        heap = []
        ans = 0

        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])

            if s[i] == '1':
                ans += -heapq.heappop(heap)

        return ans