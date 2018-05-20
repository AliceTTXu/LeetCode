class TreeNode(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.nums = nums
        self.root = self.__seg_tree(0, len(nums) - 1)

    def __seg_tree(self, start, end):
        if start > end:
            return None
        
        node = TreeNode(start, end)

        if start == end:
            node.sum = self.nums[start]
            return node

        mid = (start + end) / 2
        node.left = self.__seg_tree(start, mid)
        node.right = self.__seg_tree(mid + 1, end)

        node.sum = node.left.sum + node.right.sum

        return node

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

        diff = val - self.nums[i]
        self.nums[i] = val

        node = self.root
        while node:
            node.sum += diff
            mid = (node.start + node.end) / 2
            if i <= mid:
                node = node.left
            else:
                node = node.right

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        
        return self.__sum_helper(self.root, i, j)

    def __sum_helper(self, node, i, j):
        if i == node.start and j == node.end:
            return node.sum
        
        mid = (node.start + node.end) / 2
        if i > mid:
            return self.__sum_helper(node.right, i, j)
        elif j <= mid:
            return self.__sum_helper(node.left, i, j)
        else:
            return self.__sum_helper(node.left, i, mid) + self.__sum_helper(node.right, mid + 1, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)