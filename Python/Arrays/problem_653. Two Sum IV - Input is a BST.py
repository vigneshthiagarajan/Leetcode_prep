# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        list_node_vals = []
        inorder(root, list_node_vals)
        pointer1 = 0
        pointer2 = len(list_node_vals) - 1
        while (pointer1 != pointer2):
            total = list_node_vals[pointer1] + list_node_vals[pointer2]
            if (total == k):
                return True
            if (total < k):
                pointer1 += 1
            else:
                pointer2 -= 1
        return False


def inorder(root, list_node_vals):
    if (root == None):
        return
    inorder(root.left, list_node_vals)
    list_node_vals.append(root.val)
    inorder(root.right, list_node_vals)
