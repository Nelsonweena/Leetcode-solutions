class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
    
        result = ""
        cycle = 2 * numRows - 2

        for r in range(numRows):
            step1 = 2 * (numRows - r - 1)
            step2 = 2 * r
            pointer = r
            useStep1 = True

            while pointer < len(s):
                result += s[pointer]

                if useStep1:
                    jump = step1
                else:
                    jump = step2

                if jump == 0:
                    jump = step1 + step2

                pointer += jump
                useStep1 = not useStep1   

        return result
        