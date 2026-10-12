class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        curr = dummy
        num1 = self.reverse(l1)
        num2 = self.reverse(l2)
        sum  = num1 + num2

        if sum == 0:
            return ListNode(0)
    
        while sum != 0:
            temp = sum % 10
            curr.next = ListNode(temp)
            curr = curr.next
            sum = sum // 10
        
        return dummy.next

    def reverse(self, list):
        out = 0
        count = 0
        while list:
            out += list.val * (10 ** count)
            list = list.next
            count += 1
        return out 