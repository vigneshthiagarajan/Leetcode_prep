class Solution:
    def reverse_whole(self, lst: list, left: int, right: int) -> None:
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

    def reverse_word(self, lst: list):
        n = len(lst)
        start = 0
        end = 0
        while(start < n):
            while(end < n and lst[end] != " "):
                end += 1
            self.reverse_whole(lst, start, end - 1)
            start = end + 1
            end += 1

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse_whole(s, 0, len(s) - 1)
        self.reverse_word(s)
