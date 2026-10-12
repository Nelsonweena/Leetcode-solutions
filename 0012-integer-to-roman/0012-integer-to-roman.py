class Solution(object):
    def intToRoman(self, num):
        arr = [
            ("M", 1000), ("CM", 900),
            ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90),
            ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9),
            ("V", 5), ("IV", 4),
            ("I", 1)
        ]
        
        result = ""
        counter = 0
        while num:
            val = num // arr[counter][1]
            temp = arr[counter][0] * val
            result += temp
            num -= val * arr[counter][1] 
            counter += 1
        
        return result