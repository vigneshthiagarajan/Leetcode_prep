class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        pointer1 = 0
        pointer2 = 0
        ans = []
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums1[pointer1] == nums2[pointer2]:
                ans.append(nums1[pointer1])
                pointer1 += 1
                pointer2 += 1
            elif nums1[pointer1] > nums2[pointer2]:
                pointer2 += 1
            else:
                pointer1 += 1
        return ans
