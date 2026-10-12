class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            current_sum = a + b

            # Default: every pair needs 2 moves
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # For sums from low to high, only 1 move needed
            diff[low] -= 1
            diff[high + 1] += 1

            # For current_sum, 0 moves needed
            diff[current_sum] -= 1
            diff[current_sum + 1] += 1

        ans = float('inf')
        moves = 0

        for target_sum in range(2, 2 * limit + 1):
            moves += diff[target_sum]
            ans = min(ans, moves)

        return ans