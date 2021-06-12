class Solution:
    def reverseWords(self, s: str) -> str:
        return_string = ""
        s = s.split(" ")
        for word_index in range(len(s)):
            word = s[word_index]
            if word_index == len(s) - 1:
                return_string += word[::-1]
            else:
                return_string += word[::-1] + " "
        return return_string

