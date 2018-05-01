# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0

        self.out = 0
        self.helper(root)

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0

        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0

        self.out = max(self.out, left + right)

        return max(left, right)