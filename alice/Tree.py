class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def DFS(p):
	s = []
	s.append(p)
	while s:
		n = s.pop()
		print(n.val)
		if n.right:
			s.append(n.right)
		if n.left:
			s.append(n.left)

def BFS(p):
	q = []
	q.append(p)
	while q:
		n = q.pop(0)
		print(n.val)
		if n.left:
			q.append(n.left)
		if n.right:
			q.append(n.right)

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

DFS(n1)
BFS(n1)