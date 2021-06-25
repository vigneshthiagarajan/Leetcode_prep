class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10, 
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
}
        total = 0
        pointer = 0
        while(pointer < len(s)):
            if pointer + 1 < len(s) and values[s[pointer]] < values[s[pointer + 1]]:
                total += values[s[pointer + 1]] - values[s[pointer]]
                pointer += 2
            else:
                total += values[s[pointer]]
                pointer += 1
        return total
    
                

        