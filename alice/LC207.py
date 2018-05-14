from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        counts = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        visit_order = []

        for edge in prerequisites:
            counts[edge[0]] += 1
            graph[edge[1]].append(edge[0])

        queue = deque()
        for i, x in enumerate(counts):
            if x == 0:
                visit_order.append(i)
                queue.append(i)

        while queue:
            current_node = queue.popleft()
            for node in graph[current_node]:
                counts[node] -= 1
                if counts[node] == 0:
                    visit_order.append(node)
                    queue.append(node)

        return len(visit_order) == numCourses
