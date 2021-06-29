class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        # case if lenghts are not same, then they cant be buddy strings
        if len(s) != len(goal):
            return False

        # If s is equal to goal, then if any characters are repeating, we can swap them
        # and make them buddy strings
        if s == goal:
            existing = set()
            for a in s:
                if a in existing:
                    return True
                existing.add(a)
            return False

        # Otherwise make sure there are exactly two pairs of
        # Different characters existing between the two strings which are
        # The reverse of each other
        pairs = []
        for i, j in zip(s, goal):
            print(pairs)
            if i != j:
                pairs.append([i, j])
            if len(pairs) > 2:
                return False

        if len(pairs) == 2:
            if pairs[0] == pairs[1][::-1]:
                return True
        return False
