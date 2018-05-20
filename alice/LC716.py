class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack = []
        self.max_stack = []
        self.count = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        self.stack.append(x)
        if self.max_stack:
            self.max_stack.append(max(self.max_stack[-1], x))
        else:
            self.max_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        
        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        
        return self.max_stack[-1]

    def popMax(self):
        """
        :rtype: int
        """
        
        self.count += 1
        
        cache = []
        target_max = self.max_stack[-1]

        while self.stack and self.stack[-1] != target_max:
            cache.append(self.stack.pop())
            self.max_stack.pop()

        self.stack.pop()
        self.max_stack.pop()

        for c in cache[::-1]:
            self.push(c)

        return target_max

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()