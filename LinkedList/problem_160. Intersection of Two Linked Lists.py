# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        #         # HashSet solution
        #         #   Store nodes of list B as values in a hashset

        #         nodes_in_B = set()
        #         while(headB != None):
        #             nodes_in_B.add(headB)
        #             headB = headB.next

        #         # Go through A and find the point of intersection

        #         while(headA != None):
        #             if(headA in nodes_in_B):
        #                 return headA
        #             headA = headA.next

        #         return None

        # Two pointer method

        length_a = 0
        length_b = 0

        # Get lengths of linkedlists

        temp_head_a = headA
        temp_head_b = headB

        while(temp_head_a != None):
            length_a += 1
            temp_head_a = temp_head_a.next

        while(temp_head_b != None):
            length_b += 1
            temp_head_b = temp_head_b.next

        if(length_a > length_b):
            length_diff = length_a - length_b

            pointerA = headA
            pointerB = headB

            count = 0
            while(count < length_diff):
                pointerA = pointerA.next
                count += 1

            while(pointerA != None):
                if(pointerA == pointerB):
                    return pointerA
                pointerA = pointerA.next
                pointerB = pointerB.next

        if(length_b >= length_a):
            length_diff = length_b - length_a

            pointerA = headA
            pointerB = headB

            count = 0
            while(count < length_diff):
                pointerB = pointerB.next
                print(pointerB.val)
                print(headB.val)
                count += 1

            while(pointerB != None):
                if(pointerA == pointerB):
                    return pointerB
                pointerA = pointerA.next
                pointerB = pointerB.next

            return None
