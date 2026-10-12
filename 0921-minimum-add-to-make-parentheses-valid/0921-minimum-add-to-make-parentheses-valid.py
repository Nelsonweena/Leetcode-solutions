class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        need = 0
        for c in s:
            if c == '(':
                need += 1
            elif c == ')':
                need -= 1
                if need < 0:
                    ans += 1
                    need = 0

        return ans + need
    
