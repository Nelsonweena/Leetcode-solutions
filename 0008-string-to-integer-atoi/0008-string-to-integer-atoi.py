class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        ans = 0

        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            ans = ans * 10 + digit
            i += 1

        ans *= sign

        return max(-2**31, min(ans, 2**31 - 1))