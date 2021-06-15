class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        months_dict = {month : order+1 for order, month in enumerate(months)}
        components = date.split(" ")
        return components[2] + "-" + "{:02d}".format(months_dict[components[1]]) + "-" + "{:02d}".format(int(components[0][:-2])) 