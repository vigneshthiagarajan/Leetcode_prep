class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        length = len(word)

        match_1, match_2_3 = True, True

        # case 1: All caps
        for i in range(length):
            if not word[i].isupper():
                match_1 = False
                break
        if match_1:
            return True

        # case 3 : all chars after first one are lower case

        for i in range(1, length):
            if word[i].isupper():
                match_2_3 = False
                break
        if match_2_3:
            return True

        return False
