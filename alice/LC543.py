# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.diameter = 0
        self.find_depth(root)

        return self.diameter


    def find_depth(self, root):
        if not root:
            return 0

        left_max_depth = self.find_depth(root.left)
        right_max_depth = self.find_depth(root.right)

        temp = left_max_depth + right_max_depth + 2
        if temp > self.diameter:
            self.diameter = temp

        return max(left_max_depth, right_max_depth) + 1