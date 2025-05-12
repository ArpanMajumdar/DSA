from heapq import heappush, heappop


class MedianOfStream:
    def __init__(self):
        self.num_values = 0
        self.small_heap = [] # max heap
        self.large_heap = [] # min heap
        self.current_median = 0

    # This function should take a number and store it
    def insert_num(self, num):
        self.current_median = self.find_median()
        if len(self.small_heap) == 0 and len(self.large_heap) == 0:
            heappush(self.small_heap, -num)
            self.current_median = num

        elif num < self.current_median:
            heappush(self.small_heap, -num)
            self.rebalance_heaps()

        else:
            heappush(self.large_heap, num)
            self.rebalance_heaps()

        print(f"{self.small_heap=}")
        print(f"{self.large_heap=}")

        self.num_values += 1

    def rebalance_heaps(self):
        if len(self.small_heap) > len(self.large_heap) + 1:
            num = -heappop(self.small_heap)
            heappush(self.large_heap, num)

        elif len(self.large_heap) > len(self.small_heap):
            num = heappop(self.large_heap)
            heappush(self.small_heap, -num)

    # This function should return the median of the stored numbers
    def find_median(self):
        # Replace this placeholder return statement with your code
        if len(self.small_heap) == 0:
            pass
        elif self.num_values % 2 == 0:
            self.current_median = (-self.small_heap[0] + self.large_heap[0]) / 2
        else:
            self.current_median = -self.small_heap[0]

        return self.current_median


if __name__ == "__main__":
    mos = MedianOfStream()

    nums = [3, 2, 3, 4, 5, 6, 1]
    for num in nums:
        mos.insert_num(num)
        print(f"current_median={mos.find_median()}")
        print()
