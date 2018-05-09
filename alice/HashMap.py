# Double linked list class to store key-value pairs with the same key hash
class ListNode(object):
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.next = None
        self.pre = None

# Hash map class
class HashMap:
    def __init__(self, size=11):
        """Allocate an array of length size to store key-value pairs
        Key-value pair is stored at the index of the hash of key mod size
        """
        self.storage = [ListNode(None, None) for _ in range(size)]
        self.size = size
        
    def __compute_index__(self, key):
        """Compute the hash of key mod size, aka the index key corresponds to
        """
        try:
            return hash(key) % self.size
        except TypeError:
            print "TypeError: Unsupported key type"
            return
        
    def __find_node__(self, head, key):
        """Find the location of the key-value pair in the linked list
        """
        while head:
            if head.key == key:
                return head
            head = head.next
        else:
            return
        
    def add(self, key, value):
        """Insert key-value pair to the HashMap, overwrite if already exists
        """
        index = self.__compute_index__(key)
        if index is None:
            return
        old_node = self.__find_node__(self.storage[index], key)
        new_node = ListNode(key, value)
        if old_node is None:
            pre_node = self.storage[index]
            nxt_node = pre_node.next
        else:
            pre_node = old_node.pre
            nxt_node = old_node.next
        pre_node.next, new_node.next = new_node, nxt_node
        new_node.pre = pre_node
        if nxt_node:
            nxt_node.pre = new_node
        
    def get(self, key):
        """Return the value of the key-value pair with the same input key
        """
        index = self.__compute_index__(key)
        if index is None:
            return
        temp_node = self.__find_node__(self.storage[index], key)
        if temp_node is None:
            print "KeyError: Key does not exist in this HashMap"
            return
        else:
            return temp_node.val
        
    def delete(self, key):
        """Remove the key-value pair with the same input key from the HashMap 
        """
        index = self.__compute_index__(key)
        if index is None:
            return
        temp_node = self.__find_node__(self.storage[index], key)
        if temp_node is None:
            print "KeyError: Key does not exist in this HashMap"
        else:
            pre_node = temp_node.pre
            nxt_node = temp_node.next
            pre_node.next = nxt_node
            if nxt_node:
                nxt_node.pre = pre_node

    def has_key(self, key):
        """Chech if there exists a key-value pair with the same input key
        """
        index = self.__compute_index__(key)
        if index is None:
            return
        temp_node = self.__find_node__(self.storage[index], key)
        if temp_node is None:
            return False
        else:
            return True

    def keys(self):
        """Return all the existing keys in the HashMap
        """
        all_keys = []
        for head in self.storage:
            while head.next:
                head = head.next
                all_keys.append(head.key)
        return all_keys

    def values(self):
        """Return all the existing values in the HashMap
        """
        all_vals = []
        for head in self.storage:
            while head.next:
                head = head.next
                all_vals.append(head.val)
        return all_vals

    def clear(self):
        """Reinitialize the HashMap
        """
        self.__init__(size=self.size)

tt = HashMap()
tt.delete(1)
print tt.keys()
tt.add(2, 3)
print tt.keys()
tt.get(2)
print tt.keys()
tt.get(3)
print tt.keys()
tt.add('123', 324)
print tt.keys()
tt.clear()
print tt.keys()

for i in xrange(20):
    tt.add(str(i), i)

for i, x in enumerate(tt.storage):
    while x.next:
        print i, x.next.val
        x = x.next
