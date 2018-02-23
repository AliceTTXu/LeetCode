Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        currentNode = head
        flagNode = None
        count = 0

        while currentNode.next:
            if count == n:
                flagNode = flagNode.next
                currentNode = currentNode.next
            else:
                count += 1
                currentNode = currentNode.next
                if count == n:
                    flagNode = head

        if flagNode == None:
            return head.next
        else:
            flagNode.next = flagNode.next.next
            return head