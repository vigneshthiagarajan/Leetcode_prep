class Solution:
    def balancedStringSplit(self, s: str) -> int:
        iterator = 0
        resultant = 0
        for letter in s:
            iterator = iterator + 1 if letter == 'L' else iterator - 1
            if (iterator == 0):
                resultant = resultant + 1
        return resultant
