# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        initialNode = ListNode(0)
        currentNode = initialNode
        plusOne = 0

        while l1 and l2:
            temp = l1.val + l2.val + plusOne
            if temp >= 10:
                currentNode.next = ListNode(temp - 10)
                plusOne = 1
            else:
                currentNode.next = ListNode(temp)
                plusOne = 0

            l1 = l1.next
            l2 = l2.next
            currentNode = currentNode.next

        rest = l1 or l2

        if rest == None and plusOne == 1:
            currentNode.next = ListNode(1)
            plusOne = 0

        if rest != None and plusOne == 0:
            currentNode.next = rest

        while plusOne == 1:
            if rest == None:
                currentNode.next = ListNode(1)
                plusOne = 0
                break

            temp = rest.val + plusOne
            if temp >= 10:
                currentNode.next = ListNode(temp - 10)
                plusOne = 1

            else:
                currentNode.next = ListNode(temp)
                plusOne = 0

            rest = rest.next
            currentNode = currentNode.next

        if rest != None:
            currentNode.next = rest

        return initialNode.next
            
