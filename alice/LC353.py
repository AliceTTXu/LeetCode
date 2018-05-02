from collections import deque

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """

        self.food = food
        self.snake = deque([(0, 0)])
        self.height = height
        self.width = width
        self.score = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        
        head = self.snake[-1]
        next_head = self.__next_step(head, direction)

        if next_head == -1:
            return -1

        if self.score < len(self.food) and list(next_head) == self.food[self.score]:
            self.score += 1
        else:
            self.snake.popleft()
        
        if next_head in self.snake:
            return -1

        self.snake.append(next_head)
        
        return self.score

    def __next_step(self, head, direction):
        if direction == 'U':
            if head[0] == 0:
                return -1
            temp_head = (head[0] - 1, head[1])
        elif direction == 'L':
            if head[1] == 0:
                return -1
            temp_head = (head[0], head[1] - 1)
        elif direction == 'R':
            if head[1] == self.width - 1:
                return -1
            temp_head = (head[0], head[1] + 1)
        elif direction == 'D':
            if head[0] == self.height - 1:
                return -1
            temp_head = (head[0] + 1, head[1])

        return temp_head

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)