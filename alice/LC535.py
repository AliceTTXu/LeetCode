import random

class Codec:

    lookup_dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """

        candidates = [str(i) for i in range(10)] \
            + [chr(i + ord('a')) for i in range(26)] \
            + [chr(i + ord('A')) for i in range(26)]

        short = ''.join(random.sample(candidates, 6))
        while short in self.lookup_dict:
            short = ''.join(random.sample(candidates, 6))

        self.lookup_dict[short] = longUrl

        return 'http://tinyurl.com/' + short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """

        return self.lookup_dict[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))