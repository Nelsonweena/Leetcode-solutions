from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        queue = deque([s])
        visited = {s}
        ans = []

        while queue and not ans:
            for _ in range(len(queue)):
                curr = queue.popleft()

                l = 0
                r = 0
                valid = True

                for c in curr:
                    if c == '(':
                        l += 1
                    elif c == ')':
                        r += 1
                    if r > l:
                        valid = False
                        break

                if l == r and valid:
                    ans.append(curr)

                if ans:
                    continue
                
                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue
                    
                    new_s = curr[:i] + curr[i+1:]

                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append(new_s)
        
        return ans