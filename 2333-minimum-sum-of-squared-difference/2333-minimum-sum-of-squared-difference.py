class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(d) <= k:
            return 0

        l, r = 0, max(d)
        while l < r:
            m = (l + r) // 2
            if sum(max(0, x - m) for x in d) <= k:
                r = m
            else:
                l = m + 1

        k -= sum(max(0, x - l) for x in d)
        d = [min(x, l) for x in d]

        return sum(x*x for x in d) - k * (2*l - 1)