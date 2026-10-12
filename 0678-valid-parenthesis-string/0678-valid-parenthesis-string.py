class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n):
            for j in range(n + 1):
                if not dp[i][j]:
                    continue

                c = s[i]
                if c == '(':
                    if j < n:
                        dp[i + 1][j + 1] = True
                elif c == ')':
                    if j > 0:
                        dp[i + 1][j - 1] = True
                else:
                    dp[i + 1][j] = True
                    if j < n:
                        dp[i + 1][j + 1] = True
                    if j > 0:
                        dp[i + 1][j - 1] = True
        
        return dp[n][0]
