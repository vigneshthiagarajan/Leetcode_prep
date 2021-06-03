# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        # HashSet solution
        #   Store nodes of list B as values in a hashset

        nodes_in_B = set()
        while(headB != None):
            nodes_in_B.add(headB)
            headB = headB.next

        # Go through A and find the point of intersection

        while(headA != None):
            if(headA in nodes_in_B):
                return headA
            headA = headA.next

        return None
