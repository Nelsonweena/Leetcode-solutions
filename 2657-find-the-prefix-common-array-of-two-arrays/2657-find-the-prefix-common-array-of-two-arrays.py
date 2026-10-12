class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = []
        setA = set()
        setB = set()
        n = len(A)
        
        for i in range(n):
            setA.add(A[i])
            setB.add(B[i])
            res.append(len(setA & setB))
        
        return res
