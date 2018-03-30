# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return
        
        previous_node = None

        while head:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node

        return previous_node
