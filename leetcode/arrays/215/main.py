class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums = sorted(nums, reverse=True) # Solução 1 ( pior ), O(n log n)
        return nums[k - 1]

        """heap = [] # solução 2, O(n log k)

        for n in nums:
            heapq.heappush(heap, n)

            if len(heap) > k:
                heapq.heappop(heap)

            return heap[0]"""