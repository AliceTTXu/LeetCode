class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        while len(nums1) > m:
            nums1.pop()
        nums1.extend([0 for i in range(n)])

        while n and m:
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
        if n:
            for i in xrange(n):
                nums1[i] = nums2[i]


s = Solution()
s.merge([5,6,7,8], 4, [1,2,3], 3)