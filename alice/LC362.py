class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.timestamps = range(300)
        self.hits = [0] * 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        
        index = timestamp % 300
        if timestamp == self.timestamps[index]:
            self.hits[index] += 1
        else:
            self.timestamps[index] = timestamp
            self.hits[index] = 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        
        return sum([self.hits[i] for i in range(300) if timestamp - self.timestamps[i] < 300])

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)