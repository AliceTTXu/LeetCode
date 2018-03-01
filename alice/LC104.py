# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.DFS(root, 0)

    def DFS(self, node, count):
        if not node:
            return count
        else:
            return max(self.DFS(node.left, count + 1), self.DFS(node.right, count + 1))

    def maxDepth1(self, root):

        if not root:
            return 0

        prev = [root]
        curr = []
        count = 0
        while prev:
            for x in prev:
                if x.left:
                    curr.append(x.left)
                if x.right:
                    curr.append(x.right)
            prev = curr
            count += 1
            curr = []

        return count

    def maxDepth2(self, root):

        if not root:
            return 0

        stack = [root]
        depth = [1]
        out = 1

        while stack:
            currentNode = stack.pop()
            currentDepth = depth.pop()
            out = max(out, currentDepth)
            if currentNode.left:
                stack.append(currentNode.left)
                depth.append(currentDepth + 1)
            if currentNode.right:
                stack.append(currentNode.right)
                depth.append(currentDepth + 1)

        return out



