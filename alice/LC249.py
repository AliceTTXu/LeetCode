class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        out_dict = {}

        for string in strings:
            k_string = tuple([(ord(x) - ord(string[0])) % 26 for x in string])
            out_dict[k_string] = out_dict.get(k_string, []) + [string]

        return out_dict.values()
