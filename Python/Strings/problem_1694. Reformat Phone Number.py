class Solution:
    def reformatNumber(self, number: str) -> str:
        output_string = ""
        number = number.replace(" ", "")
        number = number.replace("-", "")
        while len(number) > 4:
            output_string = output_string + number[:3] + "-"
            number = number[3:]
        if len(number) == 4:
            return output_string + number[:2] + "-" + number[2:]
        # elif(len(number) == 3):
        #     return output_string + number
        # else:
        #     return output_string + number
        # Decomposing above to single case
        else:
            return output_string + number
