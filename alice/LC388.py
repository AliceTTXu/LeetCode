class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        depth_lenth_dict = {0: 0}
        out_max = 0
        
        lines = input.splitlines()
        for one_line in lines:
            len_name = len(one_line.lstrip('\t'))
            depth = (len(one_line) - len_name)
            if '.' in one_line:
                out_max = max(out_max, depth_lenth_dict[depth] + len_name)
            else:
                depth_lenth_dict[depth + 1] = depth_lenth_dict[depth] + len_name + 1
        return out_max


s = Solution()
print s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")