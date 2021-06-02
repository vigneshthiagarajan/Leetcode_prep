class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        # case if lenghts are not same, then they cant be buddy strings
        if (len(s) != len(goal)):
            return False

        # If s is equal to goal, then if any characters are repeating, we can swap them
        # and make them buddy strings
        if (s == goal):
            existing = set()
            for a in s:
                if a in existing:
                    return True
                existing.add(s)
            return False

        pairs = []

        for i, j in zip(s, goal):
            print(i, j)


