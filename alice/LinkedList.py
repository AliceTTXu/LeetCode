# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def getVal(self):
    	return self.val

    def getNext(self):
    	return self.next

    def setVal(self, newValue):
    	self.val = newValue

    def setNext(self, newNext):
    	self.next = newNext

# s = ListNode(1)
# s.setNext(ListNode(2))
# print s.getNext().getVal()

dummy = current = ListNode(0)

current.next = ListNode(1)
current = ListNode(3)

print dummy.val
print dummy.next.val
print current.val
