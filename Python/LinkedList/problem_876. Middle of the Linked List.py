# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        temp = head
        while temp != None:
            temp = temp.next
            length += 1
        mid = math.floor(length / 2)

        count = 0
        while count < mid:
            head = head.next
            count += 1
        return head
