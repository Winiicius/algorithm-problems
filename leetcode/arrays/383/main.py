class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dic = {}

        for l in ransomNote:
            dic[l] = dic.get(l, 0) + 1

        for l in magazine:
            if l in dic and dic[l] != 0:
                dic[l] = dic[l] - 1

        return all(x == 0 for x in dic.values())


print(Solution().canConstruct("aaabcc", "aaabcccaaaa"))
