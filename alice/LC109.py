# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        n = 0
        fake_head = head
        while fake_head:
            n += 1
            fake_head = fake_head.next

        self.node = head

        return self.binary_search(0, n)


    def binary_search(self, l, r):

        if l > r:
            return None

        m = l + (r - l) / 2
        left_node = self.binary_search(l, m - 1)
        root = TreeNode(self.node.val)
        self.node = self.node.next
        root.left = left_node
        root.right = self.binary_search(m + 1, r)

        return root