# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # This isn't actual deleting, but seems to be the solution they are
        # looking for
        node.val = node.next.val
        node.next = node.next.next
