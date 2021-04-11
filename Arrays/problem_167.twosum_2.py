class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_1 = 0
        pointer_2 = len(numbers)-1
        while(pointer_1 != pointer_2):
            print(pointer_1, pointer_2)
            sum_of_the_two = numbers[pointer_1] + numbers[pointer_2]
            if(sum_of_the_two == target):
                return [pointer_1 + 1 , pointer_2 + 1]
            elif(sum_of_the_two < target):
                pointer_1 += 1
            else:
                pointer_2 -= 1