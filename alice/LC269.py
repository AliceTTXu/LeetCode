import Queue

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        if not words or not words[0]:
            return ''
        
        graph = {}
        counts = {}
        seen = set()

        for x in words[0]:
            counts[x] = 0
            graph[x] = set()

        for i, word in enumerate(words[1:], 1):
            for x in word:
                if x not in counts:
                    counts[x] = 0
                    graph[x] = set()

            edge = self.find_first_diff(words[i - 1], word)
            if not edge and len(words[i - 1]) > len(word):
                return ''

            if edge and edge not in seen:
                seen.add(edge)
                counts[edge[1]] += 1
                graph[edge[0]].add(edge[1])

        visit_order = []
        queue = Queue.Queue()

        for x in counts:
            if counts[x] == 0:
                queue.put(x)
                visit_order.append(x)

        while not queue.empty():
            current_s = queue.get()
            for x in graph[current_s]:
                counts[x] -= 1
                if counts[x] == 0:
                    queue.put(x)
                    visit_order.append(x)

        return ''.join(visit_order) if len(visit_order) == len(counts) else ''

    def find_first_diff(self, word1, word2):
        for s1, s2 in zip(word1, word2):
            if s1 != s2:
                return (s1, s2)
