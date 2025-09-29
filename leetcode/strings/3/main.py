class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        atual = ""
        for i, char in enumerate(s, 1):
            melhor = max(melhor, len(atual))
            atual = ""
            atual += char
            for char2 in s[i:]:
                if char2 not in atual:
                    atual+=char2
                else:
                    break
        return melhor

sequencia = input()

print(Solution().lengthOfLongestSubstring(sequencia))