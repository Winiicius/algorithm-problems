class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        mset = set(nums)
        maior_seq = 0
        print(mset)

        for n in mset:
            seq_atual = 1
            if n - 1 in mset:
                continue
            while n + 1 in mset:
                seq_atual += 1
                n = n + 1
            maior_seq = seq_atual if seq_atual > maior_seq else maior_seq
        return maior_seq


print(Solution().longestConsecutive([0, -1]))
