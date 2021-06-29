class Solution:
    def removeDuplicates(self, s: str) -> str:
        # changed = True
        # while(changed == True):
        #     changed = False
        #     idx = 0
        #     while(idx < len(s)-1):
        #         if(s[idx] == s[idx+1]):
        #             s = s[:idx] + s[idx+2:]
        #             changed = True
        #         idx+=1
        # return s

        # faster - generate 26 possible duplicates
        duplicates = [2 * ch for ch in ascii_lowercase]

        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            for d in duplicates:
                s = s.replace(d, "")

        return s
