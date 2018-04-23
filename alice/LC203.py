# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        head0 = ListNode(0)
        head0.next = head
        pre = head0
        
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
            
        return head0.next