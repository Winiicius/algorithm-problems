class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):  # minha solução
            pd = len(nums) - 1
            pl = i + 1
            while pl <= pd:
                if nums[i] + nums[pd] == target:
                    return [i, pd]
                if nums[i] + nums[pl] == target:
                    return [i, pl]

                pl += 1
                pd -= 1


""" # Solução Otimizada
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
"""


lista = [3, 2, 4]
target = 6
print(Solution().twoSum(lista, target))
