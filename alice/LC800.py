class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        
        out = '#'

        for i in range(3):
            out += self.find_lest_square(color[2 * i + 1:2 * (i + 1) + 1])

        return out

    def find_lest_square(self, one_channel):
        first_digit = int(one_channel[0], 16)
        second_digit = int(one_channel[1], 16)
        candidates = set([max(0, first_digit - 1), first_digit, min(first_digit + 1, 15)])
        temp_min_ls, winner = None, None

        for x in candidates:
            temp = ((first_digit * 16 + second_digit) - (x * 16 + x)) ** 2
            if temp_min_ls is None or temp < temp_min_ls:
                temp_min_ls, winner = temp, x

        return hex(winner)[-1] * 2