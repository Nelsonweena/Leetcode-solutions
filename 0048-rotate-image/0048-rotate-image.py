class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        result = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                result[r][c] = matrix[c][r]

        for r in range(n):
            temp = [0] * n
            for c in range(n):
                temp[c] = result[r][n - 1 - c]
            result[r] = temp

        for r in range(n):
            for c in range(n):
                matrix[r][c] = result[r][c]