from heapq import heapify, heappush, heappop

# Solution
# 1. Push all capitals values in a min-heap.
# 2. Select projects that can be invested in the range of the current capital and push their profits in a max-heap.
# 3. Select the project from the max-heap that yields the maximum profit.
# 4. Add the profit from the selected project to the current capital.


def maximum_capital(c: int, k: int, capitals: list[int], profits: list[int]):
    curr_inv = c

    for _ in range(k):
        capitals_min_heap = []
        profits_max_heap = []

        for i, capital in enumerate(capitals):
            heappush(capitals_min_heap, (capital, i))

        while len(capitals_min_heap) > 0 and capitals_min_heap[0][0] <= curr_inv:
            capital, i = heappop(capitals_min_heap)
            heappush(profits_max_heap, (-profits[i], i))

        if len(profits_max_heap) == 0:
            break

        max_profit, i = heappop(profits_max_heap)
        max_profit = -max_profit
        curr_inv += max_profit

        capitals.pop(i)
        profits.pop(i)

    return curr_inv


if __name__ == "__main__":
    k = 3
    c = 2
    capitals = [1, 2, 3, 4]
    profits = [1, 3, 5, 7]
    sol = maximum_capital(c, k, capitals, profits)
    print(f"{sol=}")
