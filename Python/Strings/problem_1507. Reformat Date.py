class Solution:
    def reformatDate(self, date: str) -> str:
        months = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        months_dict = {month: order + 1 for order, month in enumerate(months)}
        components = date.split(" ")
        return (
            components[2]
            + "-"
            + "{:02d}".format(months_dict[components[1]])
            + "-"
            + "{:02d}".format(int(components[0][:-2]))
        )


# class Solution:
#     def reformatDate(self, date: str) -> str:
#         def make_2digit(digit):
#             return digit if len(digit) == 2 else f'0{digit}'

#         day, month, year = date.split()

#         month_mapping = {
#             'Jan': '01',
#             'Feb': '02',
#             'Mar': '03',
#             'Apr': '04',
#             'May': '05',
#             'Jun': '06',
#             'Jul': '07',
#             'Aug': '08',
#             'Sep': '09',
#             'Oct': '10',
#             'Nov': '11',
#             'Dec': '12',
#         }

#         day_digit = ''
#         for char in day:
#             if char.isdigit():
#                 day_digit += char
#             else:
#                 break

#         return f'{year}-{month_mapping[month]}-{make_2digit(day_digit)}'
