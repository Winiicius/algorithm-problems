from typing import List

class Solution:
    def twoSum(self, numeros: List[int], alvo: int) -> List[int]:

        esquerdo = 0

        direito = len(numeros) - 1

        while direito > esquerdo:

            soma = numeros[esquerdo] + numeros[direito]

            if soma == alvo: return [esquerdo+1, direito+1]

            elif soma > alvo: direito-=1
            
            else: esquerdo += 1

# Entrada
# linha 1 ( lista de numeros ) -> 2 7 11 15
# linha 2 ( numero alvo ) -> 9
numeros = list(map(int, input().split()))
numero_alvo = int(input())

print(Solution().twoSum(numeros=numeros, alvo=numero_alvo))