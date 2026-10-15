from typing import List


class Solution:  # minha solução
    def subarraySum(self, nums: List[int], k: int) -> int:
        subArrays = 0

        for i, n in enumerate(nums):
            soma = 0

            for j in range(i, len(nums)):
                soma += nums[j]

                if soma == k:
                    subArrays += 1

        return subArrays


class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subArrays = 0
        soma = 0
        dic = {0: 1}

        for n in nums:
            soma += n

            subArrays += dic.get(soma - k, 0)

            dic[soma] = dic.get(soma, 0) + 1

        return subArrays


print(Solution2().subarraySum([3, 9, 5, 2, 6], 7))
