class Codec:
    mapper = dict()
    index = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        mapper[index] = longUrl
        encoded = "http://tinyurl.com/" + str(index)
        index += 1
        return encoded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))