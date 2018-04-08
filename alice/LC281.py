class ZigzagIterator(object):

    def __init__(self, v1, v2, v3):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """

        self.position = [0] * 3
        self.mega = [v1, v2, v3]
        self.current_v = 0

    def next(self):
        """
        :rtype: int
        """
        
        while True:
            if self.position[self.current_v] < len(self.mega[self.current_v]):
                out = self.mega[self.current_v][self.position[self.current_v]]
                self.update_current_v()
                return out
            else:
                self.update_current_v()

    def hasNext(self):
        """
        :rtype: bool
        """
        
        for i in xrange(len(self.position)):
            if self.position[i] < len(self.mega[i]):
                return True

        return False

    def update_current_v(self):
        self.position[self.current_v] += 1
        self.current_v = (self.current_v + 1) % len(self.position)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator([1,2,3], [4,5,6,7], [8,9]), []
# while i.hasNext(): v.append(i.next())