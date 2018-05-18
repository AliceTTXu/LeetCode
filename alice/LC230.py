# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        count = 0
        head = root
        stack = []

        while head or stack:
            while head:
                stack.append(head)
                head = head.left
            head = stack.pop()
            count += 1
            if count == k:
                return head.val
            head = head.right
