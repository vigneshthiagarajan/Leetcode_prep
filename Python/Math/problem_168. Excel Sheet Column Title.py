class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabets = list(alphabets)
        title = ""
        while(columnNumber > 0):
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            title = alphabets[remainder] + title
        return title
            
