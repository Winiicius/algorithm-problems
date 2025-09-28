from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic:dict = {}
        for anagrama in strs:
            anagrama_ordenado = "".join(sorted(anagrama))
            if (anagrama_ordenado in list(dic.keys())):
                dic[anagrama_ordenado].append(anagrama)
            else:
                dic[anagrama_ordenado] = [anagrama]
        return list(dic.values())

# Exemplo entrada: eat tea tan ate nat bat
strings = list(map(str, input().split()))

print(Solution().groupAnagrams(strings))