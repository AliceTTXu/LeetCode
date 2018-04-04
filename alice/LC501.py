# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.tally = {}
        
        self.inorder(root)

        temp_max = 0
        out = []

        for x in self.tally:
            if self.tally[x] > temp_max:
                out = [x]
                temp_max = self.tally[x]
            elif self.tally[x] == temp_max:
                out.append(x)

        return out

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        self.tally[root.val] = self.tally.get(root.val) + 1
        self.inorder(root.right)


