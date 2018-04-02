# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        dummy = current = ListNode(0)
        kList = []

        while head:
            kList.append(head)
            head = head.next
            if len(kList) == k:
                while kList:
                    temp = kList.pop()
                    current.next = temp
                    current = current.next
                    temp.next = None

        if kList:
            current.next = kList[0]

        return dummy.next