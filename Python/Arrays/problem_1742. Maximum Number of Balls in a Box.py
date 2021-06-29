class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        mapper = {}
        for ball_num in range(lowLimit, highLimit + 1):
            ball_sum_digits = sum(list(map(int, str(ball_num))))
            if ball_sum_digits not in mapper:
                mapper[ball_sum_digits] = 1
            else:
                mapper[ball_sum_digits] += 1
        max_box = max(mapper.values())
        return max_box
