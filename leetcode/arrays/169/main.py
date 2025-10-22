from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        dic = sorted(dic.items(), key=lambda item: -item[1])
        print(dic)

        return dic[0][0]
        
nums = list(map(int, input().split()))


print(Solution().majorityElement(nums=nums))


# IA Algotimo de Boyer-Moore
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = None
#         count = 0

#         for n in nums:
#             if count == 0:
#                 candidate = n
#             count += (1 if n == candidate else -1)
        
#         return candidate