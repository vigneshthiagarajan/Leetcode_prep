# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        num1 = l1
        num2 = l2
        current = dummy_head
        propagate = 0
        while(num1 != None or num2 != None):
            if(num1 == None):
                num1_digit = 0
            else:
                num1_digit = num1.val
            if(num2 == None):
                num2_digit = 0
            else:
                num2_digit = num2.val
            sum_of_nums = num1_digit + num2_digit + propagate
            propagate = sum_of_nums // 10
            current.next = ListNode(sum_of_nums % 10)
            current = current.next
            if(num1 != None):
                num1 = num1.next
            if(num2 != None):
                num2 = num2.next
            if(propagate > 0):
                current.next = ListNode(1)
        return dummy_head.next
            
            
        