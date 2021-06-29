# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        head = current = TreeNode(None)
        for i in self.inorder(root, self.arr):
            current.right = TreeNode(i.val)
            current = current.right
        return head.right

    def inorder(self, root: TreeNode, arr):
        if not root.left and not root.right:
            arr.append(root)
            return arr
        if root.left:
            self.inorder(root.left, arr)
        if root:
            arr.append(root)
        if root.right:
            self.inorder(root.right, arr)
        return arr
