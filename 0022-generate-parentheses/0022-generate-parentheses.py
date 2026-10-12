class Solution(object):
    def generateParenthesis(self, n):
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                for a in dp[j]:
                    for b in dp[i - 1 - j]:
                        dp[i].append("(" + a + ")" + b)

        return dp[n]