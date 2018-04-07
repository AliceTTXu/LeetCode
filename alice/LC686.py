class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """


        temp_out = len(B) / len(A)
        end = self.find_substring_ending(A * (temp_out + 2), B)

        if end == -1:
            return -1
        else:
            return temp_out + ((end + 1) - len(A) * temp_out) / len(A) + (((end + 1) - len(A) * temp_out) % len(A) > 0)           

    def find_substring_ending(self, A, B):
        for i in xrange(len(A) - len(B) + 1):
            if A[i:i + len(B)] == B:
                return i + len(B) - 1
        return -1
