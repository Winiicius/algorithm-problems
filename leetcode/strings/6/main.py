class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        cycle = 2 * (numRows - 1)
        res = []

        for i in range(numRows):
            for j in range(i, len(s), cycle):
                res.append(s[j])
                diag = j + cycle - 2 * i
                if 0 < i < numRows - 1 and diag < len(s):
                    res.append(s[diag])

        return ''.join(res)
    

# Como usar:
# PAIEHFHEU 3
s, numRows = map(str, input().split())
print(Solution().convert(s, int(3)))  # "PAHNAPLSIIGYIR"
