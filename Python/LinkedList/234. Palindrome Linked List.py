# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        string_repr = ""
        while head != None:
            string_repr += str(head.val)
            head = head.next
        if string_repr[::-1] == string_repr:
            return True
        else:
            return False
