class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        vertical = 0
        horizontal = 0

        for x in moves:
            if x == "R":
                horizontal += 1
            elif x == "L":
                horizontal -= 1
            elif x == "U":
                vertical += 1
            else:
                vertical -= 1

        return vertical == 0 and horizontal == 0