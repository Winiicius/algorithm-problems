class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hist = set()
        for n in nums:
            if n in hist:
                return True
            hist.add(n)
        return False


print(Solution().containsDuplicate([1, 2, 3, 4, 5, 6, 67, 10, 45, 34, 2]))
