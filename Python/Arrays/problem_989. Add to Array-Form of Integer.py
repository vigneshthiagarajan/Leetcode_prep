class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(i) for i in num]
        num = int("".join(num))
        num_sum = num + k
        return_list = []
        while num_sum > 0:
            num_sum, digit = divmod(num_sum, 10)
            return_list.insert(0, digit)
        if not return_list:
            return_list = [0]
        return return_list
