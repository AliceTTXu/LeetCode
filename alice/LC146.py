class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.key_node_dict = {}
        self.capacity = capacity
        self.head = DoubleListNode(0, 0)
        self.tail = DoubleListNode(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        n = -1
        if key in self.key_node_dict:
            n = self.key_node_dict[key].val
            self._remove(key)
            self._add(key, n)
        return n

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.key_node_dict:
            self._remove(key)
        self._add(key, value)
        if len(self.key_node_dict) > self.capacity:
            self.key_node_dict.pop(self.head.next.key)
            node = self.head.next.next
            self.head.next = node
            node.previous = self.head
        
    def _add(self, key, value):
        node = DoubleListNode(key, value)
        pre = self.tail.previous
        pre.next = node
        node.previous = pre
        node.next = self.tail
        self.tail.previous = node
        self.key_node_dict[key] = node

    def _remove(self, key):
        node = self.key_node_dict.pop(key)
        pre = node.previous
        nxt = node.next
        pre.next = nxt
        nxt.previous = pre

class DoubleListNode(object):
    def __init__(self, x, y):
        self.val = y
        self.key = x
        self.next = None
        self.previous = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)