import collections

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        
        self.seen = {}
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])
        self.destination = destination

        queue = collections.deque()
        steps = collections.deque()
        queue.append(start)
        steps.append(0)
        self.seen[tuple(start)] = 0

        while queue:
            current_position = queue.popleft()
            current_step = self.seen[tuple(current_position)]
            next_positions = self.find_next_position(current_position, current_step)
            queue.extend(next_positions)

        return self.seen.get(tuple(destination), -1)

    def find_next_position(self, current, current_step):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        next_positions = []

        for move in moves:
            [x, y] = current
            steps = 0
            while 0 <= (x + move[0]) < self.height and 0 <= (y + move[1]) < self.width and self.maze[x + move[0]][y + move[1]] != 1:
                x += move[0]
                y += move[1]
                steps += 1

            if (x, y) not in self.seen or self.seen[(x, y)] > current_step + steps:
                self.seen[(x, y)] = current_step + steps
                if (x, y) != tuple(self.destination):
                    next_positions.append([x, y])

        return next_positions