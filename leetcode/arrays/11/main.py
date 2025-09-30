from typing import List

class Solution:
    def maxArea(self, alturas: List[int]) -> int:
        l, r = 0, len(alturas) - 1
        max_area = 0

        while l < r:
            h = min(alturas[l], alturas[r])
            area = h * (r - l)
            if area > max_area:
                max_area = area

            # mover o ponteiro da menor altura
            if alturas[l] < alturas[r]:
                l += 1
            elif alturas[l] > alturas[r]:
                r -= 1
            else:
                l += 1

        return max_area
    
alturas = [1,8,6,2,5,4,8,3,7]

print(Solution().maxArea(alturas))
