class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        diff_s1 = []
        diff_s2 = []
        count_different = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count_different += 1
                diff_s1.append(s1[i])
                diff_s2.append(s2[i])
                if count_different > 2:
                    return False
        if (count_different == 2) or (count_different == 0):
            if sorted(s1) == sorted(s2):
                return True
        return False
