class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        list_return = []
        counts  = collections.Counter(nums)
        for key, val in counts.items():
            if val > len(nums) // 3:
                list_return.append(key)
        return list_return