class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if len(trust) < n - 1:
            return -1

        indegree = [0 for i in range(n + 1)]
        outdegree = [0 for i in range(n + 1)]

        for s, d in trust:
            outdegree[s] += 1
            indegree[d] += 1

        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1
