from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = []
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            esquerdo = i+1
            direito = len(nums) - 1
            
            while esquerdo < direito:
                soma = nums[i] + nums[esquerdo] + nums[direito]
                if soma == 0:
                    triplets.append([nums[i], nums[esquerdo], nums[direito]])
                    while esquerdo < direito and nums[esquerdo] == nums[esquerdo + 1]:
                            esquerdo += 1
                    while esquerdo < direito and nums[direito] == nums[direito - 1]:
                        direito -= 1

                    esquerdo += 1
                    direito -= 1
                elif soma < 0: esquerdo += 1
                else: direito -= 1
        return triplets
    
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))



        