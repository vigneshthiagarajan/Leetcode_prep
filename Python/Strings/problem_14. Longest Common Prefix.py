class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        stringPrefix = strs[0]
        for i in range(1, len(strs)):
            while(strs[i].find(stringPrefix) != 0):
                stringPrefix = stringPrefix[:-1]
                if(stringPrefix == ""):
                    return ""
        return stringPrefix
