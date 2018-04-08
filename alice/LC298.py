# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        self.out = 1
        self.DFS(root, root.val, 1)

        return self.out

    def DFS(self, current_node, parent_val, temp_len):
        if not current_node:
            return

        if current_node.val == parent_val + 1:
            self.out = max(self.out, temp_len + 1)
            self.DFS(current_node.left, current_node.val, temp_len + 1)
            self.DFS(current_node.right, current_node.val, temp_len + 1)
        else:
            self.DFS(current_node.left, current_node.val, 1)
            self.DFS(current_node.right, current_node.val, 1)