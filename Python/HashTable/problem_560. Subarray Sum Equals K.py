class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute force
        # counts = 0
        # length = len(nums)
        # for start in range(length):
        #     for end in range(start + 1, length + 1):
        #         sum_subarray = 0
        #         for i in range(start, end):
        #             sum_subarray += nums[i]
        #         if(sum_subarray == k):
        #                 counts += 1
        # return counts

        # counts = 0
        # length = len(nums)
        # sum_array = [0 for i in range(length+1)]
        # for i in range(1, length+1):
        #     sum_array[i] = sum_array[i-1] + nums[i-1]
        # for start in range(length):
        #     for end in range(start + 1, length + 1):
        #         sum_subarray = sum_array[end] - sum_array[start]
        #         if(sum_subarray == k):
        #                 counts += 1
        # return counts

        count, cum_sum = 0, 0
        mapper = defaultdict(int)
        mapper[0] = 1
        for i in range(len(nums)):
            cum_sum += nums[i]
            if(cum_sum - k in mapper):
                count += mapper[cum_sum - k]
            mapper[cum_sum] += 1
        return count
