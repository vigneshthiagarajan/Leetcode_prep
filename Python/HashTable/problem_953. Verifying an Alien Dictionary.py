class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_chars = {}
        for idx, val in enumerate(order):
            order_chars[val] = idx

        for i in range(len(words) - 1):

            for j in range(len(words[i])):

                # Account for index from 0
                if j > len(words[i + 1]) - 1:
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_chars[words[i][j]] > order_chars[words[i + 1][j]]:
                        return False
                    break
        return True
