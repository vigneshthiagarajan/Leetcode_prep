class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dictionaryCities = dict()
        for i in range(len(paths)):
            dictionaryCities[paths[i][0]] = paths[i][1]

        current_city = paths[0][0]
        while (current_city in dictionaryCities):
            current_city = dictionaryCities[current_city]
        return current_city