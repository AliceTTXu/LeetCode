import collections

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        
        self.seen = set()
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])

        queue = collections.deque()
        queue.append(start)
        self.seen.add(tuple(start))

        while queue:
            current_position = queue.popleft()
            next_positions = self.find_next_position(current_position)
            if tuple(destination) in self.seen:
                return True
            queue.extend(next_positions)

        return False

    def find_next_position(self, current):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        next_positions = []

        for move in moves:
            [x, y] = current
            while 0 <= (x + move[0]) < self.height \
                and 0 <= (y + move[1]) < self.width \
                and self.maze[x + move[0]][y + move[1]] != 1:
                x += move[0]
                y += move[1]

            if (x, y) not in self.seen:
                self.seen.add((x, y))
                next_positions.append([x, y])

        return next_positions