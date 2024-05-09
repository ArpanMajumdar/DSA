from typing import List

# Key takeaways:
# - Use sliding window method
# - Keep track of the lowest price before the current price and update the max profit


class Solution:
    # Brute force
    def maxProfitBruteForce(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        i = 0
        j = 1
        n = len(prices)

        while j < n:
            print(f"i={i}, price_i = {prices[i]}, j={j}, price_j = {prices[j]}")
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
            else:
                i = j

            j += 1

        return max_profit

    def maxProfitSoln2(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for price in prices:
            lowest_price = min(price, lowest_price)
            profit = price - lowest_price
            max_profit = max(profit, max_profit)

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
    res = sol.maxProfitSoln2(prices)
    print(f"prices = {prices}")
    print(f"res = {res}")
