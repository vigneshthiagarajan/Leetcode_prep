# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest_diff = math.inf
        closest_value = math.inf
        while root != None:
            value_diff = root.val - target
            abs_diff = abs(value_diff)
            if value_diff == 0:
                return int(target)
            if value_diff < 0:
                if abs_diff < closest_diff:
                    closest_value = root.val
                    closest_diff = abs_diff
                root = root.right

            if value_diff >= 0:
                if abs_diff < closest_diff:
                    closest_diff = abs_diff
                    closest_value = root.val
                root = root.left

        return int(closest_value)
