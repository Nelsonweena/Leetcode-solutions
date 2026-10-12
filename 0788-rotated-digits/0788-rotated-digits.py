class Solution(object):
    def rotatedDigits(self, n):
        count = 0

        for num in range(1, n + 1):
            s = str(num)

            if any(ch in s for ch in "347"):
                continue

            if any(ch in s for ch in "2569"):
                count += 1

        return count