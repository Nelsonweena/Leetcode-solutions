class Solution(object):
    def isValid(self, s):
        stack = []
        matching = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in matching.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != matching[c]:
                    return False
        
        return not stack
        