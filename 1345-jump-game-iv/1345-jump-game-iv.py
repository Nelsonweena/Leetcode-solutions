from collections import deque

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return 0
        
        pos = {}
        visited = set([0])
        q = deque([0])
        steps = 0

        for i, val in enumerate(arr):
            if val not in pos:
                pos[val] = []
            pos[val].append(i)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == n - 1:
                    return steps
                
                neighbours = []

                if curr - 1 >= 0:
                    neighbours.append(curr - 1)
                
                if curr + 1 < n:
                    neighbours.append(curr + 1)

                neighbours.extend(pos[arr[curr]])

                pos[arr[curr]] = []

                for nxt in neighbours:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            
            steps += 1
        
        return -1
            
        
        