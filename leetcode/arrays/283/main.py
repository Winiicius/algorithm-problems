from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ultimo_zero_em = 0

        for indice_atual in range(len(nums)):
            if nums[indice_atual] != 0:
                nums[ultimo_zero_em], nums[indice_atual] = nums[indice_atual], nums[ultimo_zero_em]
                ultimo_zero_em += 1
        
    

nums = list(map(int, input().split()))
Solution().moveZeroes(nums)
print(nums)