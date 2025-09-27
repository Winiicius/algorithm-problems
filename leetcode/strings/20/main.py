class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(":")", "[":"]", "{":"}"}

        fila = []

        for i in s:
            if i == ")" or i == "]" or i == "}":
                if len(fila) > 0 and dic[fila[-1]] == i:
                    fila.pop()
                else: return False
            else:
                fila.append(i)
        if(len(fila) == 0): return True;
        return False

s = str(input())

print(Solution().isValid(s=s))
        
        