class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return_string = ""
        pointer1 = len(num1) - 1
        pointer2 = len(num2) - 1
        propagate = 0
        while(pointer1 >= 0 or pointer2 >= 0):
            if(pointer1 >= 0):
                num1_digit = int(num1[pointer1])
            else:
                num1_digit = 0
            if(pointer2 >= 0):
                num2_digit = int(num2[pointer2])
            else:
                num2_digit = 0
            sum_digits = num1_digit + num2_digit + propagate
            propagate = sum_digits // 10
            digit_req = sum_digits % 10
            return_string = str(digit_req) + return_string
            pointer1 -= 1
            pointer2 -= 1
        if(propagate > 0):
            return_string = "1" + return_string
        return return_string
