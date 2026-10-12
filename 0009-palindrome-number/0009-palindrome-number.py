class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev = self.reverse(x)
        return x == rev
    
    def reverse(self, x):
        int_max = 2**31 - 1
        int_min = -2**31

        sign = -1 if x < 0 else 1
        x *= sign

        rev = 0
        while x:
            digit = x % 10
            x //= 10

            if rev > int_max // 10 or (rev == int_max // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit
        
        return sign * rev
        