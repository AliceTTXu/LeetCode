# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        stack = []
        head0 = None
        node0 = ListNode(0)

        flag = True

        while head:
            if flag:
                head0 = head 
            if not stack:
                stack.append(head)     
                head = head.next
            else:
                node1 = stack.pop()
                nextNode = head.next

                node0.next = head
                head.next = node1
                node1.next = nextNode
                head = nextNode
                node0 = node1
                if flag:
                    flag = False


        return head0

    def swapPairs1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        stack = []
        head0 = node0 = ListNode(0)
        head0.next = head

        while head:

            if not stack:
                stack.append(head)     
                head = head.next
            else:
                node1 = stack.pop()
                nextNode = head.next

                node0.next = head
                head.next = node1
                node1.next = nextNode
                head = nextNode
                node0 = node1


        return head0.next



