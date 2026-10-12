class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        count = 0
        left = 0
        right = 0
        for action in moves:
            if action == 'L':
                left += 1
            elif action == 'R': 
                right += 1
            else:
                count += 1
        
        return count + max(left, right) - min(left, right)