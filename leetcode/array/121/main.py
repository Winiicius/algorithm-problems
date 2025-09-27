from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # menor preço até agora
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit  # atualiza lucro máximo
        
        return max_profit

# entrada -> 1 2 3 4 5 6 ( lista de numeros separados por espaços)
lista = list(map(int, input().split()))

print(Solution().maxProfit(lista))