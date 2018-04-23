# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        head0 = ListNode(None)
        head0.next = head
        pre, temp, cur_val = head0, head, None
        flag = False
        
        while head:

            if cur_val is None:
                cur_val = head.val
                head = head.next
            else:
                if head.val != cur_val:
                    if flag == False:
                        pre.next = temp
                        pre = temp
                    temp = head
                    flag = False
                    cur_val = head.val
                else:
                    flag = True
                head = head.next
       
        if flag == False:
            pre.next = temp
        else:
            pre.next = None
          
        return head0.next
            