# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        current = dummy

        h = [(x.val, x) for x in lists if x]
        heapq.heapify(h)

        while h:
            val, node = heapq.heappop(h)
            current.next = node
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))
            current = node

        return dummy.next