class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = ""
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            title = alphabet_char[remainder] + title
        return title
