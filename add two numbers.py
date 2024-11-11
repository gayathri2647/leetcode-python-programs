class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  
        current = dummy
        carry = 0

        while l1 or l2 or carry:
              val1 = l1.val if l1 else 0
              val2 = l2.val if l2 else 0
              total = val1 + val2 + carry
              carry = total // 10
              new_digit = total % 10

              current.next = ListNode(new_digit)
              current = current.next

              # Move to the next nodes in the lists, if available
              if l1: l1 = l1.next
              if l2: l2 = l2.next

        return dummy.next
 
        
