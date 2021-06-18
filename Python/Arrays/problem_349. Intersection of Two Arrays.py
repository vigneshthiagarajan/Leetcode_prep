class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return_array = []
        set1 = set(nums1)
        set2 = set(nums2)
        for i in list(set1):
            if i in set2:
                return_array.append(i)
        return return_array