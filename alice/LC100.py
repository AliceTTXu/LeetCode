# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # try:
        #     print p.val
        # except AttributeError:
        #     print p
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (p != None and q == None):
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False

    

    def isSameTree2(self, p, q):

        pStack = []
        qStack = []

        while pStack or p:
            while p:
                if q == None:
                    return False
                pStack.append(p)
                qStack.append(q)
                p = p.left
                q = q.left
            if q:
                return False
            p = pStack.pop()
            q = qStack.pop()
            if p.val != q.val:
                return False
            p = p.right
            q = q.right

        if qStack or q:
            return False

        return 

    def isSameTree3(self, p, q):

        stack = [(p, q)]

        while stack:
            (pCurrent, qCurrent) = stack.pop()
            if pCurrent and qCurrent:
                if pCurrent.val == qCurrent.val:
                    stack.append((pCurrent.right, qCurrent.right))
                    stack.append((pCurrent.left, qCurrent.left))
                else:
                    return False
            elif not pCurrent and not qCurrent:
                continue
            else:
                return False

        return True



nn1 = TreeNode(2)
nn2 = TreeNode(3)
nn3 = TreeNode(4)

mm1 = TreeNode(2)
mm2 = TreeNode(4)

nn1.left = nn2
nn1.right = nn3

mm1.right = mm2

s = Solution()
print s.isSameTree3(mm1, nn1)


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

m1 = TreeNode(1)
m2 = TreeNode(2)
m3 = TreeNode(3)
m4 = TreeNode(4)
m5 = TreeNode(5)
m6 = TreeNode(6)
m1.left = m2
m1.right = m3
m3.left = m4
m3.right = m5
m5.right = m6

s = Solution()
print s.isSameTree3(n1, m1)


