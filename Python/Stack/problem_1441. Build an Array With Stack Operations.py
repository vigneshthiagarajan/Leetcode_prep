class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        list_output = []
        i, j = 1, 0

        while i < n + 1:
            if target[j] == i:
                list_output.append("Push")
                j += 1
            else:
                list_output.append("Push")
                list_output.append("Pop")
            if j == len(target):
                break
            i += 1
        return list_output
