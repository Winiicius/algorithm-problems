from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}
        soma = 0
        maior = 0

        for i, n in enumerate(nums):
            if n == 0:
                soma -= 1
            else:
                soma += 1

            if soma in dic:
                tamanho = i - dic[soma]
                maior = max(maior, tamanho)
            else:
                dic[soma] = i

        return maior
