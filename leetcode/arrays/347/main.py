class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq:dict = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        freq = sorted(freq.items(), key=lambda item: -item[1])

        # import heapq
        # top = heapq.nlargest(k, freq.items(), key=lambda item: item[1])
        # return [n[0] for n in top]

        return [n[0] for n in freq[:k]]

Solution().topKFrequent([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 5], 2)