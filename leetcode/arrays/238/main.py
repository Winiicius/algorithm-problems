from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        atual = 1
        final = []
        for n in nums:
            indice = nums.index(n)
            for i in nums:
                if nums.index(i) == indice:
                    continue
                atual *= i
            final.append(atual)
        return final

print(Solution().productExceptSelf([0,0]))

