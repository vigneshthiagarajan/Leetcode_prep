class Codec:
    mapper = dict()
    index = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.mapper[self.index] = longUrl
        self.encoded = "http://tinyurl.com/" + str(self.index)
        self.index += 1
        print(self.encoded)
        return self.encoded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        decoded_index = shortUrl.split("http://tinyurl.com/")[1]
        decoded_index = int(decoded_index)
        return self.mapper[decoded_index]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
