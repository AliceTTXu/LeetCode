# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        return self.symmetricCore(root.left, root.right)
        

    def symmetricCore(self, l, r):
        if not l and not r:
            return True
        elif not l or not r:
            return False
        elif l.val == r.val:
            return self.symmetricCore(l.left, r.right) and self.symmetricCore(l.right, r.left)
        else:
            return False

