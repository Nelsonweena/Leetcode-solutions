class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        nums_new = []
        for i in range(len(nums)):
            temp = nums[i]
            e = 0
            while temp > 0:
                e += temp % 10
                temp = temp // 10
            nums_new.append(e)

        n = len(nums)

        # Sort by digit sum, then by number
        sorted_nums = sorted(range(n), key=lambda i: (nums_new[i], nums[i]))

        # Find target position of each original index
        pos = [0] * n
        for i, idx in enumerate(sorted_nums):
            pos[idx] = i

        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = pos[j]
                cycle += 1

            ans += cycle - 1

        return ans