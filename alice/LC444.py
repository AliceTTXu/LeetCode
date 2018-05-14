import Queue

class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        
        counts = [0] * (len(org) + 1)
        graph = [set() for _ in range(len(org) + 1)]
        seen = set()
        
        for seq in seqs:
            if len(seq) == 1:
                if not (0 < seq[0] <= len(org)):
                    return False
                else:
                    seen.add(seq[0])
            for i in xrange(0, len(seq) - 1):
                if not (0 < seq[i] <= len(org)) or not (0 < seq[i + 1] <= len(org)):
                    return False
                seen.add(seq[i])
                seen.add(seq[i + 1])
                if seq[i + 1] not in graph[seq[i]]:
                    counts[seq[i + 1]] += 1
                    graph[seq[i]].add(seq[i + 1])

        if len(seen) != len(org):
            return False
      
        visiting_order = []
        queue = Queue.Queue()
        
        for i, x in enumerate(counts[1:], 1):
            if x == 0:
                visiting_order.append(i)
                queue.put(i)
                
        if queue.qsize() != 1:
            return False

        while not queue.empty():
            current_node = queue.get()
            candidate = []
            for node in graph[current_node]:
                counts[node] -= 1
                if counts[node] == 0:
                    candidate.append(node)

            if len(candidate) > 1:
                return False
            elif len(candidate) == 1:
                queue.put(candidate[0])
                visiting_order.append(candidate[0])
       
        return visiting_order == org
 