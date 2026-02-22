from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final_list = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                final_list[idx] = i - idx
            stack.append(i)
        return final_list
            
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
