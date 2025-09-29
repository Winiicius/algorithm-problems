from typing import List

class Solution:
    def merge(self, intervalos: List[List[int]]) -> List[List[int]]:
        intervalos = sorted(intervalos, key=lambda x: x[0])
        resultado = []
        for i, intervalo in enumerate(intervalos, 1):
            if not resultado or resultado[-1][1] < intervalo[0]:
                resultado.append(intervalo)
            else:
                resultado[-1][1] = max(resultado[-1][1], intervalo[1])

        return resultado

# intervalos = [[1,3],[2,6],[8,10],[15,18]]
intervalos = [[1,4],[0,2],[3,5]]
# intervalos = [[4,7],[1,4]]

print(Solution().merge(intervalos))