# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        visited = []
        self.inorderCore(root, visited)
        return visited

    def inorderCore(self, root, visited):

        if root:
            self.inorderCore(root.left, visited)
            visited.append(root.val)
            self.inorderCore(root.right, visited)

    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        out = []
        current = root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            out.append(current.val)
            current = current.right

        return out


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
n5.right = n6

s = Solution()
print s.inorderTraversal2(n1)
print s.inorderTraversal2(None)