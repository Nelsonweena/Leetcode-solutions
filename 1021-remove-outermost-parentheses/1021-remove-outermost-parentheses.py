class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        l = 0
        for c in s:
            if c == '(':
                if l > 0:
                    ans += c
                l += 1
            else:
                l -= 1
                if l > 0:
                    ans += c

        return ans



        