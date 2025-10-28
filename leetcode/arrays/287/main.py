from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)

# Algoritmo de Floyd
def findDuplicateFloyd(self, nums: List[int]) -> int: # Fase 1: detectar o encontro (como se fosse lista com ciclo)
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Fase 2: encontrar a "entrada" do ciclo = número duplicado
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
