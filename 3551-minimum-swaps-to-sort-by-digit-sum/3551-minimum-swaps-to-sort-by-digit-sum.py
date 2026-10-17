class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digitSum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digitSum(x), x))

        pos = {num: i for i, num in enumerate(sorted_nums)}
        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle += 1

            ans += cycle - 1

        return ans