from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)

        stack = [] 
        best = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                x = heights[stack[-1]]
                top = stack.pop()
                height = heights[top]

                left_smaller = stack[-1] if stack else -1
                right_smaller = i 

                width = right_smaller - left_smaller - 1
                best = max(best, height * width)

            stack.append(i)

        heights.pop()
        return best
    
print(Solution().largestRectangleArea([2,1,5,6,2,3]))