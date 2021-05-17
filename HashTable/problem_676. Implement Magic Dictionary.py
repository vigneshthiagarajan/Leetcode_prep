class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_set = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.dict_set = set(dictionary)

    def search(self, searchWord: str) -> bool:
        dict_words = self.dict_set
        for word in dict_words:
            if len(word) != len(searchWord) or word == searchWord:
                continue
            else:
                count = 0
                for i in range(len(word)):
                    if (word[i] != searchWord[i]):
                        count += 1
                    if (count >= 2):
                        break
                if count == 1:
                    return True
        return False


