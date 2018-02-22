# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        initialNode = ListNode(0)
        currentNode = initialNode

        while l1 and l2:

            if l1.val <= l2.val:
                currentNode.next = l1
                l1 = l1.next
            else:
                currentNode.next = l2
                l2 = l2.next

        currentNode.next = l1 or l2

        return initialNode.next
