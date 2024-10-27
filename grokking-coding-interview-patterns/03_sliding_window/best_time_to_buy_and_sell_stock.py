# Problem
# Given an array where the element at the index i represents the price of a stock on day i, find the maximum profit that you can gain by buying the stock once and then selling it.
# Constraints
# 1 <= prices.length <= 10^3
# 0 <= prices[i] <= 10^5


def max_profit(prices: list[int]) -> int:
    n = len(prices)
    max_profit = 0
    buy_price = float("inf")

    for i in range(n):
        buy_price = min(buy_price, prices[i])
        profit = prices[i] - buy_price
        max_profit = max(max_profit, profit)
        # print(f"buy_price = {buy_price}, sell_price = {prices[i]}, profit = {profit}, max_profit = {max_profit}")
    return max_profit

if __name__ == "__main__":
    inputs = [
        {"prices": [7,1,5,3,6,4]},
        {"prices": [10, 8, 6, 4, 2]},
        {"prices": [10,4,11,1,5]},
        {"prices": [7,7,6,6,6]},
    ]

    for input in inputs:
        output = max_profit(input["prices"])
        print(f"prices = {input["prices"]}")
        print(f"output = {output}")
        print()
