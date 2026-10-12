from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        visited = set([start])
        q = deque([start])
        while q:
            curr = q.popleft()

            if arr[curr] == 0:
                return True
            
            for next in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next < n and next not in visited:
                    visited.add(next)
                    q.append(next)
            
        return False
        
            