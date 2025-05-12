from heapq import heapify, heappop, heappush

# nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 5


def median_sliding_window(nums: list[int], k: int) -> list[float]:
    # Declare a min and max heap to store elements of the sliding window
    small_nums_max_heap = []
    large_nums_min_heap = []
    output = []

    # Push k elements into the max heap and transfer k/2 elements to the min heap
    for i in range(k):
        heappush(small_nums_max_heap, -nums[i])

    for i in range(k // 2):
        heappush(large_nums_min_heap, -heappop(small_nums_max_heap))

    curr_median = calc_median(small_nums_max_heap, large_nums_min_heap, k)
    output.append(curr_median)

    # print(
    #     f"window={nums[0:k]}, {small_nums_max_heap=}, {large_nums_min_heap=}, {curr_median=}"
    # )

    # Move the sliding window forward and rebalance the heaps
    n = len(nums)
    for i in range(1, n - k + 1):
        incoming_num = nums[i + k - 1]
        outgoing_num = nums[i - 1]

        # If incoming num < max_heap[0], push to max heap. Else push num to min heap.
        if incoming_num <= -small_nums_max_heap[0]:
            heappush(small_nums_max_heap, -incoming_num)
        else:
            heappush(large_nums_min_heap, incoming_num)

        rebalance_heaps(small_nums_max_heap, large_nums_min_heap)

        # If outgoing num is at top of either heaps, remove it from heap.
        if outgoing_num <= -small_nums_max_heap[0]: 
            small_nums_max_heap.remove(-outgoing_num)
            heapify(small_nums_max_heap)
        else:
            large_nums_min_heap.remove(outgoing_num)
            heapify(large_nums_min_heap)

        rebalance_heaps(small_nums_max_heap, large_nums_min_heap)

        curr_median = calc_median(small_nums_max_heap, large_nums_min_heap, k)
        # print(
        #     f"window={nums[i : i + k]}, {small_nums_max_heap=}, {large_nums_min_heap=}, {curr_median=}"
        # )

        output.append(curr_median)

    return output


def calc_median(small_nums_max_heap, large_nums_min_heap, k):
    if k % 2 == 0:
        median = (-small_nums_max_heap[0] + large_nums_min_heap[0]) / 2
    else:
        median = -small_nums_max_heap[0]
    return median


def rebalance_heaps(small_nums_max_heap, large_nums_min_heap):
    while len(large_nums_min_heap) > len(small_nums_max_heap):
        heappush(small_nums_max_heap, -heappop(large_nums_min_heap))

    while len(small_nums_max_heap) > len(large_nums_min_heap) + 1:
        heappush(large_nums_min_heap, -heappop(small_nums_max_heap))


if __name__ == "__main__":
    nums = [1, 3, -1, 2, -2, -3, 5, 1, 5, 3]
    k = 4
    output = median_sliding_window(nums, k)
    print(f"{nums=}, {k=}")
    print(f"{output=}")
