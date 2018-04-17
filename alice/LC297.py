# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return ''

        out = str(root.val)
        queue = [root]

        while queue:
            cur = queue.pop(0)
            if cur.left:
                out += '|' + str(cur.left.val)
                queue.append(cur.left)
            else:
                out += '|'
            if cur.right:
                out += '|' + str(cur.right.val)
                queue.append(cur.right)
            else:
                out += '|'

        return out

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return

        data = data.split('|')
        root = TreeNode(int(data.pop(0)))
        queue = [root]
        while queue:
            l = data.pop(0)
            r = data.pop(0)
            cur = queue.pop(0)
            if l:
                l_n = TreeNode(int(l))
                cur.left = l_n
                queue.append(l_n)
            if r:
                r_n = TreeNode(int(r))
                cur.right = r_n
                queue.append(r_n)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))