# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Using HashMaps

        # If empty linkedlist then cycle not possible
        if(head == None):
            return False

        nodes_traversed = set()
        node = head
        while(node.next != None):
            if node in nodes_traversed:
                return True
            nodes_traversed.add(node)
            node = node.next
        return False
