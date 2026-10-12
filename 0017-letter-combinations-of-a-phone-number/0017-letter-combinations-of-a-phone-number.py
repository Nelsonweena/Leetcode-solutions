class Solution(object):
    def letterCombinations(self, digits):
        digits = str(digits)
        result = [""]
        arr = [
            "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ]
        for d in digits: 
            letters = arr[ord(d) - ord('2')]
            new_result = [] 
            
            for combi in result:
                for ch in letters:
                    new_result.append(combi + ch)
            
            result = new_result
        
        return result